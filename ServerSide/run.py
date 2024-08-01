from Scraddit import create_app # Replace with the actual import path

# Create an application instance
app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)  # You can change the port as needed
