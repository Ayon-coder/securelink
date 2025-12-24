from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI(title="Referrer-Locked Link Demo")

# Path to the protected image
IMAGE_PATH = "sydney wifu.jpeg"

@app.get("/", response_class=HTMLResponse)
async def root():
    """Root endpoint - provides information about the demo"""
    return """
    <html>
        <head>
            <title>Referrer-Locked Link Demo</title>
        </head>
        <body>
            <h1>Referrer-Locked Link Demo</h1>
            <p>Navigate to <a href="/gateway.html">Gateway Page</a> to access the protected resource.</p>
        </body>
    </html>
    """

@app.get("/gateway.html", response_class=HTMLResponse)
async def gateway():
    """Gateway page with the official link to the protected resource"""
    with open("gateway.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())

@app.get("/view-image")
async def view_image(request: Request):
    """
    Protected route that redirects to the resource only if accessed from gateway.html
    """
    # Get the Referer header from the request
    referer = request.headers.get("referer", "")
    
    print(f"[DEBUG] Referer header: {referer}")
    
    # Check if the referer contains 'gateway.html'
    if "gateway.html" in referer:
        # Valid referer - redirect to the Google Drive link
        # This "binds" the Google Drive link to our secure pathway
        google_drive_link = "https://drive.google.com/file/d/1zSvIWYWgwDArB20SLTUd5aeALB1hP4EG/view?usp=sharing"
        return RedirectResponse(url=google_drive_link)
    else:
        # Invalid or missing referer - deny access
        raise HTTPException(
            status_code=403,
            detail="Access Denied: You must use the official link from the gateway page."
        )

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "ok", "message": "Referrer-locked link system is running"}

if __name__ == "__main__":
    import uvicorn
    print("\n" + "="*50)
    print("🚀 Server Starting...")
    print("="*50)
    print("📱 Access from this computer: http://127.0.0.1:8000/gateway.html")
    print("📱 Access from mobile/other devices: http://YOUR_IP_ADDRESS:8000/gateway.html")
    print("\n💡 To find YOUR_IP_ADDRESS:")
    print("   Windows: Run 'ipconfig' and look for IPv4 Address")
    print("   Make sure mobile and computer are on the same WiFi network!")
    print("="*50 + "\n")
    uvicorn.run(app, host="0.0.0.0", port=8000)
