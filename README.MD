# 🧠 Chat Client & Server (Python)

A simple multi-client chat application built using Python sockets and threading. The server accepts multiple connections and broadcasts messages from one client to all others.

---

## 🧪 How to Run This

1. Save the server code as `server.py` and the client code as `client.py`.

2. Run the server:

    ```bash
    python server.py
    ```

3. Then run one or more clients (in separate terminals or on separate machines):

    ```bash
    python client.py
    ```

4. When prompted, enter your username and start chatting.

5. Type `exit` to leave the chat.

---

## 📦 Features

- Real-time chat
- Multiple clients over TCP
- Unique usernames
- Graceful disconnects
- `exit` command to leave

---

## ✅ Requirements

This app uses only Python's standard library. No external packages required.

Tested with **Python 3.11**

---

## 🔧 Optional: Virtual Environment Setup

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
python server.py              # or python client.py
