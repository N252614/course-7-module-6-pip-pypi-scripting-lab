from lib.generate_log import generate_log

log_data = ["User logged in", "User updated profile", "Report exported"]

if __name__ == "__main__":
    filename = generate_log(log_data)
    print(f" File '{filename}' successfully created!")