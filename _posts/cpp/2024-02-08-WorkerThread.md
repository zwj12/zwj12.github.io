---
layout: post
title: "WorkerThread"
date: 2024-02-08 10:12:00 +0800
author: Michael
categories: CPP
---

# WorkerThread.h

    #pragma once

    #include <thread>
    #include <queue>
    #include <mutex>
    #include <atomic>
    #include <condition_variable>

    using namespace std;

    #define MSG_EXIT_THREAD			1
    #define MSG_POST_USER_DATA		2
    #define MSG_TIMER				3

    struct UserData
    {
        int id;
        string data1;
        string data2;
    };

    struct ThreadMsg
    {
        ThreadMsg(int i, shared_ptr<void> m) { id = i; msg = m; }
        int id;
        shared_ptr<void> msg;
    };

    class WorkerThread
    {
    public:
        /// Constructor
        WorkerThread(const char* threadName);

        /// Destructor
        ~WorkerThread();

        /// Called once to create the worker thread
        /// @return True if thread is created. False otherwise. 
        bool CreateThread();

        /// Called once a program exit to exit the worker thread
        void ExitThread();

        /// Get the ID of this thread instance
        /// @return The worker thread ID
        thread::id GetThreadId();

        /// Get the ID of the currently executing thread
        /// @return The current thread ID
        static thread::id GetCurrentThreadId();

        /// Add a message to the thread queue
        /// @param[in] data - thread specific message information
        void PostMsg(shared_ptr<UserData> msg);

        void(*pfnExecuteCmd)(shared_ptr<UserData> data);

    private:
        WorkerThread(const WorkerThread&) = delete;
        WorkerThread& operator=(const WorkerThread&) = delete;

        /// Entry point for the worker thread
        void Process();

        /// Entry point for timer thread
        void TimerThread();

        unique_ptr<thread> m_thread;
        queue<shared_ptr<ThreadMsg>> m_queue;
        mutex m_mutex;
        condition_variable m_cv;
        atomic<bool> m_timerExit;
        const char* THREAD_NAME;

    };

# WorkerThread.cpp

    #include "pch.h"

    #include "WorkerThread.h"

    //----------------------------------------------------------------------------
    // WorkerThread
    //----------------------------------------------------------------------------
    WorkerThread::WorkerThread(const char* threadName) : m_thread(nullptr), m_timerExit(false), THREAD_NAME(threadName)
    {
        pfnExecuteCmd = nullptr;
    }

    //----------------------------------------------------------------------------
    // ~WorkerThread
    //----------------------------------------------------------------------------
    WorkerThread::~WorkerThread()
    {
        ExitThread();
    }

    //----------------------------------------------------------------------------
    // CreateThread
    //----------------------------------------------------------------------------
    bool WorkerThread::CreateThread()
    {
        if (!m_thread)
            m_thread = unique_ptr<thread>(new thread(&WorkerThread::Process, this));
        return true;
    }

    //----------------------------------------------------------------------------
    // GetThreadId
    //----------------------------------------------------------------------------
    thread::id WorkerThread::GetThreadId()
    {
        assert(m_thread != nullptr);
        return m_thread->get_id();
    }

    //----------------------------------------------------------------------------
    // GetCurrentThreadId
    //----------------------------------------------------------------------------
    thread::id WorkerThread::GetCurrentThreadId()
    {
        return this_thread::get_id();
    }

    //----------------------------------------------------------------------------
    // ExitThread
    //----------------------------------------------------------------------------
    void WorkerThread::ExitThread()
    {
        if (!m_thread)
            return;

        // Create a new ThreadMsg
        shared_ptr<UserData> userData(new UserData());
        shared_ptr<ThreadMsg> threadMsg(new ThreadMsg(MSG_EXIT_THREAD, userData));

        // Put exit thread message into the queue
        {
            lock_guard<mutex> lock(m_mutex);
            m_queue.push(threadMsg);
            m_cv.notify_one();
        }

        m_thread->join();
        m_thread = nullptr;
    }

    //----------------------------------------------------------------------------
    // PostMsg
    //----------------------------------------------------------------------------
    void WorkerThread::PostMsg(shared_ptr<UserData> data)
    {
        assert(m_thread);

        // Create a new ThreadMsg
        shared_ptr<ThreadMsg> threadMsg(new ThreadMsg(MSG_POST_USER_DATA, data));

        // Add user data msg to queue and notify worker thread
        unique_lock<mutex> lk(m_mutex);
        m_queue.push(threadMsg);
        m_cv.notify_one();
    }

    //----------------------------------------------------------------------------
    // TimerThread
    //----------------------------------------------------------------------------
    void WorkerThread::TimerThread()
    {
        while (!m_timerExit)
        {
            // Sleep for 250mS then put a MSG_TIMER into the message queue
            this_thread::sleep_for(1s);

            shared_ptr<UserData> userDataTimer(new UserData());
            userDataTimer->id = 100;
            userDataTimer->data1 = "MSG_TIMER";

            shared_ptr<ThreadMsg> threadMsg(new ThreadMsg(MSG_TIMER, userDataTimer));

            // Add timer msg to queue and notify worker thread
            unique_lock<mutex> lk(m_mutex);
            m_queue.push(threadMsg);
            m_cv.notify_one();
        }
    }

    //----------------------------------------------------------------------------
    // Process
    //----------------------------------------------------------------------------
    void WorkerThread::Process()
    {
        m_timerExit = false;
        thread timerThread(&WorkerThread::TimerThread, this);

        while (1)
        {
            shared_ptr<ThreadMsg> msg;
            {
                // Wait for a message to be added to the queue
                unique_lock<mutex> lk(m_mutex);
                while (m_queue.empty())
                    m_cv.wait(lk);

                if (m_queue.empty())
                    continue;

                msg = m_queue.front();
                m_queue.pop();
            }

            assert(msg->msg != NULL);
            //if (msg->msg == NULL) {
            //	//DebugBreak();
            //	AfxDebugBreak();
            //}
            auto userData = static_pointer_cast<UserData>(msg->msg);

            switch (msg->id)
            {
            case MSG_POST_USER_DATA:
            {
                //cout << userData->msg.c_str() << " " << userData->year << " on " << THREAD_NAME << endl;
                if (pfnExecuteCmd != NULL) {
                    pfnExecuteCmd(userData);
                }

                break;
            }

            case MSG_TIMER:
                cout << "Timer expired on " << THREAD_NAME << endl;
                if (pfnExecuteCmd != NULL) {
                    pfnExecuteCmd(userData);
                }
                break;

            case MSG_EXIT_THREAD:
            {
                m_timerExit = true;
                timerThread.join();
                return;
            }

            default:
                assert(0);
            }
        }
    }
