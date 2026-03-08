# RAG API server with FastAPI

RAG API server built with FastAPI, designed to provide a simple interface
for retrieving and generating information based on user queries.
This server can be used for various applications, including chatbots,
knowledge retrieval systems, and more.

## 📦 Requirements

- uv

## ⚙️ Setup

**Option 1: uv**:

```sh
uv sync --frozen
```

**Docker**:

```sh
docker build .
```

## 🚀 Usage

### Create configuration file

Create a `config.json` file in the working directory with the following content:

```json
{
  "host": "localhost",
  "port": 8000,
  "logLevel": "info"
}
```

| Field      | Type    | Default       | Description                                                 |
| ---------- | ------- | ------------- | ----------------------------------------------------------- |
| `host`     | string  | `"localhost"` | Hostname for the application server                         |
| `port`     | integer | `8000`        | Port number for the application server                      |
| `logLevel` | string  | `"info"`      | Logging level (`"debug"`, `"info"`, `"warning"`, `"error"`) |

All fields are optional. An empty `{}` uses the defaults.

### Run the server

**Option 1: uv**:

```sh
uv run start
```

**Docker**:

```sh
docker run -v config.json:/app/config.json:ro
```

## 📚 Reference

## 📄 License

MIT License

## 🔗 Related Projects

- [docker-rag](https://github.com/shunya-sasaki/docker-rag)
