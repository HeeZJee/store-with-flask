from src import app

#Checks if the app.py file has executed directly and not imported
if __name__ == "__main__":
    app.run(debug=True)