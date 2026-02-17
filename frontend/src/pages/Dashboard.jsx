import React, { useEffect, useState } from 'react';
import TaskForm from '../components/TaskForm';
import TaskList from '../components/TaskList';
import { getTasks } from '../api/taskApi';

const Dashboard = () => {
    const [tasks, setTasks] = useState([]);
    const [loading, setLoading] = useState(true);

    const fetchTasks = async () => {
        setLoading(true); // Optional: simplified loading for refresh
        try {
            const data = await getTasks();
            // Sort tasks by id desc
            setTasks(data.sort((a, b) => b.id - a.id));
        } catch (err) {
            console.error("Failed to fetch tasks", err);
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchTasks();
    }, []);

    return (
        <div>
            <h1>DevTrack AI</h1>
            <p>Intelligent Task Management for Developers</p>

            <TaskForm onTaskCreated={fetchTasks} />

            <h2 style={{ textAlign: 'left', marginTop: '40px' }}>Your Tasks</h2>
            {loading ? (
                <p>Loading tasks...</p>
            ) : tasks.length === 0 ? (
                <p>No tasks yet. Create one above!</p>
            ) : (
                <TaskList tasks={tasks} onTaskDeleted={fetchTasks} />
            )}
        </div>
    );
};

export default Dashboard;