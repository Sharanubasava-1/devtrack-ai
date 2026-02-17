import React from 'react';
import { deleteTask } from '../api/taskApi';

const TaskList = ({ tasks, onTaskDeleted }) => {

    const handleDelete = async (id) => {
        if (window.confirm('Are you sure you want to delete this task?')) {
            try {
                await deleteTask(id);
                if (onTaskDeleted) onTaskDeleted();
            } catch (err) {
                console.error("Failed to delete task", err);
            }
        }
    };

    const getRiskClass = (level) => {
        if (!level) return '';
        return level === 'High' ? 'risk-high' : level === 'Medium' ? 'risk-medium' : 'risk-low';
    };

    return (
        <div className="grid">
            {tasks.map((task) => (
                <div key={task.id} className="card">
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                        <h3 style={{ marginTop: 0 }}>{task.title}</h3>
                        <span className={`badge ${task.status === 'Done' ? 'risk-low' : ''}`}>{task.status}</span>
                    </div>

                    <p>{task.description}</p>

                    <div style={{ margin: '10px 0' }}>
                        <strong>AI Analysis:</strong><br />
                        <span className={`badge ${getRiskClass(task.risk_level)}`}>Risk: {task.risk_level || 'N/A'}</span>
                        <span className="badge" style={{ backgroundColor: '#333' }}>Complexity: {task.complexity || 'N/A'}</span>
                    </div>

                    {task.ai_warning && (
                        <div style={{ color: 'var(--warning-color)', fontSize: '0.9em', marginBottom: '10px' }}>
                            ⚠️ {task.ai_warning}
                        </div>
                    )}

                    <div style={{ fontSize: '0.85em', color: '#888', marginBottom: '15px' }}>
                        Due: {task.deadline ? new Date(task.deadline).toLocaleString() : 'No deadline'}
                    </div>

                    <button
                        onClick={() => handleDelete(task.id)}
                        style={{ backgroundColor: 'var(--error-color)', fontSize: '0.8em', padding: '4px 8px' }}
                    >
                        Delete
                    </button>
                </div>
            ))}
        </div>
    );
};

export default TaskList;
