@echo off

:: Step 1: Navigate to the backend directory
cd backend

:: Step 2: Run the Flask server in the background
start "" /b cmd /c "flask --app connections.server.app run"

:: Step 3: Navigate back to the root directory
cd ..

:: Step 4: Navigate to the frontend directory
cd frontend

:: Step 5: Run the frontend development server
npm run dev

:: Step 6: Pause the script to keep the console open
pause
