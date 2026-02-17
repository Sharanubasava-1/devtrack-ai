import React, { useState } from 'react';
import { createTask } from '../api/taskApi';

const TaskForm = ({ onTaskCreated }) => {
    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');
    const [deadline, setDeadline] = useState('');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError(null);
        try {
            const newTask = { title, description, deadline: deadline || null };
            await createTask(newTask);
            setTitle('');
            setDescription('');
            setDeadline('');
            if (onTaskCreated) onTaskCreated();
        } catch (err) {
            setError('Failed to create task. Please try again.');
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="card">
            <h2>Create New Task</h2>
            {error && <p style={{ color: 'var(--error-color)' }}>{error}</p>}
            <form onSubmit={handleSubmit}>
                <div style={{ display: 'flex', flexDirection: 'column' }}>
                    <label>Title</label>
                    <input
                        type="text"
                        value={title}
                        onChange={(e) => setTitle(e.target.value)}
                        required
                        placeholder="e.g., Fix login bug"
                    />

                    <label>Description (AI Analyzed)</label>
                    <textarea
                        rows="4"
                        value={description}
                        onChange={(e) => setDescription(e.target.value)}
                        placeholder="Describe the task..."
                    />

                    <label>Deadline</label>
                    <input
                        type="datetime-local"
                        value={deadline}
                        onChange={(e) => setDeadline(e.target.value)}
                    />

                    <button type="submit" disabled={loading}>
                        {loading ? 'Analyzing...' : 'Add Task'}
                    </button>
                </div>
            </form>
        </div>
    );
};

export default TaskForm;
