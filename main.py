if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app="api.v1:app", host="localhost", port=8000, debug=True, reload=True)
