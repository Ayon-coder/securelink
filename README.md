# 🔐 Referrer-Locked Link Prototype

A demonstration of referrer-based access control where a protected resource (image) can only be accessed when arriving from a specific gateway page.

## 🎯 The Concept

This prototype proves that a link is more than just a URL—it's a **pathway**. The protected image is only accessible if you arrive from the official gateway page. If you copy and paste the URL directly, access is denied.

## 🏗️ How It Works

1. **Gateway Page** (`gateway.html`): The official entry point containing a link to the protected resource
2. **Protected Route** (`/view-image`): Backend endpoint that validates the HTTP Referer header
3. **Access Control**: 
   - ✅ If Referer contains `gateway.html` → Image is served
   - ❌ Otherwise → 403 Forbidden error

## 🚀 Setup & Installation

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Server

```bash
python main.py
```

Or using uvicorn directly:

```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

The server will start at `http://127.0.0.1:8000`

## 🧪 Testing the Demo

### Test 1: Valid Access (Should Work ✅)
1. Open your browser and navigate to: `http://127.0.0.1:8000/gateway.html`
2. Click the **"View Protected Image"** button
3. The image should display successfully

### Test 2: Direct Access (Should Fail ❌)
1. Try to access: `http://127.0.0.1:8000/view-image` directly
2. You should see: **"Access Denied: You must use the official link from the gateway page."**

### Test 3: Copy-Paste URL (Should Fail ❌)
1. After successfully viewing the image from the gateway (Test 1)
2. Copy the image URL from the address bar
3. Open a new tab and paste the URL
4. Access should be denied because the referer is missing

### Test 4: Share Link (Should Fail ❌)
1. Send the `/view-image` URL to a friend
2. When they try to access it, they'll get a 403 Forbidden error
3. They must use the gateway page instead

## 📁 Project Structure

```
secure_link/
├── main.py              # FastAPI backend with referer validation
├── gateway.html         # Official gateway page
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## 🔒 Security Explanation

### Why This Works

The HTTP Referer header tells the server which page the user came from. When you:
- Click a link on `gateway.html` → Browser sends Referer: `http://127.0.0.1:8000/gateway.html`
- Directly access the URL → Browser sends no or different Referer
- Copy-paste in new tab → No Referer is sent

The backend validates this header and only grants access when the referer matches the gateway page.

### Real-World Applications

This technique demonstrates:
- 🎫 **Ticket validation systems** (concert tickets, event passes)
- 🔗 **Controlled content distribution** (authorized partners only)
- 📱 **Mobile app deep linking** (only accessible from app)
- 🌐 **Hotlink protection** (prevent image stealing)

## ⚠️ Important Notes

### Limitations
- **Not foolproof**: Advanced users can spoof the Referer header
- **Browser privacy**: Some browsers/extensions block or modify referers
- **HTTPS requirement**: For production, always use HTTPS

### Production Recommendations
For a production system, combine referer checking with:
- ✅ Token-based authentication
- ✅ Time-limited access tokens
- ✅ IP whitelisting
- ✅ Rate limiting
- ✅ Cryptographic signatures

## 🎓 Educational Value

This prototype demonstrates:
1. **HTTP Headers**: How browsers communicate context to servers
2. **Access Control**: Basic security through request validation
3. **Link Security**: Why some links only work in certain contexts
4. **Web Security**: Understanding and limitations of referer-based protection

## 🛠️ Customization

### Change the Protected Resource
Edit `main.py` line 11:
```python
IMAGE_PATH = "your-image.jpg"
```

### Modify Access Rules
Edit the validation logic in `main.py` around line 48:
```python
if "gateway.html" in referer:
    # Add additional conditions here
```

### Customize Gateway Page
Edit `gateway.html` to match your branding and messaging.

## 📊 API Endpoints

- `GET /` - Information page
- `GET /gateway.html` - Official gateway page
- `GET /view-image` - Protected image endpoint (requires valid referer)
- `GET /health` - Health check endpoint

## 💡 Next Steps

To enhance this prototype:
1. Add logging to track access attempts
2. Implement time-based token generation
3. Add user authentication layer
4. Create analytics dashboard
5. Add support for multiple protected resources

---

**Built with FastAPI** | Demonstrating pathway-based access control

