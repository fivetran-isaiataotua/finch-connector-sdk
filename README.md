# finch-connector-sdk
Connector SDK Build for Finch (tryfinch.com)
# &#x20;Finch Connector SDK Build

This  Connector fetches **employee data** from the **Finch API** and syncs it with Fivetran. Finch is a unified API for APIs from services like Gusto, BambooHR, and other HRIS and Payroll vendors.

## 🔧 Setup Instructions

### 1. Install Dependencies

```sh
pip install -r requirements.txt
```

### 2. Set Up Environment Variables

Create a `.env` file with:

```
FINCH_ACCESS_TOKEN=your_finch_api_key
```

### 3. Run the Connector

```sh
fivetran debug
```

## 🏗️ Connector Structure

- `connector.py`: Main Fivetran connector script.
- `requirements.txt`: Required Python packages.
- `.env`: Stores Finch API credentials.

## 🛠️ Debugging Issues

If you encounter `Expecting DECIMAL data type` errors:

- **Ensure all schema fields are properly typed** (`string`, `boolean`, etc.).
- **Check API response** with:
  ```sh
  python finch_debug.py
  ```
- **Try resetting files**:
  ```sh
  rm -rf /Users/your_user/finch_fivetran_connector/files/*
  ```

## 🤝 Contributing

Pull requests & issue reports are welcome!

