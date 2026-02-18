import { defineConfig, loadEnv } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig(({ mode }) => {
    // Load env file based on `mode` in the current working directory.
    // Set the third parameter to '' to load all env regardless of the `VITE_` prefix.
    const env = loadEnv(mode, process.cwd(), '')

    return {
        plugins: [react()],
        server: {
            host: true,
            port: 5173,
            proxy: {
                '/api': {
                    target: process.env.BACKEND_URL || env.BACKEND_URL || 'http://localhost:5000',
                    changeOrigin: true,
                    secure: false,
                }
            }
        }
    }
})
