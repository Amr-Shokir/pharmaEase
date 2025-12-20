from project_code import create_app

app = create_app()

if __name__ == "__main__":
    # host='0.0.0.0' allows access from outside the container
    app.run(host='0.0.0.0', debug=True)