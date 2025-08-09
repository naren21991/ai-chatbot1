**Retell AI Voice Agent Integration**
This project implements a Voice AI Agent using Retell AI with Python (FastAPI) and webhook handling.
**It supports:**
  
  Real-time call initiation
  
  Webhook-based event handling
  
  Google Sheets integration for conversation logging
  
  Knowledge Base API with 800-token chunking for accurate responses
  
  Booking & FAQ handling using NLP/function-calling

**🚀 Features**
  📲 Call Initiation API – Start calls programmatically using Retell AI.
  
  📡 Webhook Handling – Process live conversation events from Retell AI.
  
  📝 Conversation Logging – Auto-log post-call/chat data into Google Sheets.
  
  📚 Token-Limited Knowledge Base – Serve segmented responses under 800 tokens.
  
  🛡 Hallucination Prevention – Return clear “Not Found” responses for unavailable data.
  
  ⚙️ Error Handling – Covers API errors, validation issues, and fallback flows.

**🛠 Tech Stack**
  Python 3.8+
  
  FastAPI – REST API framework
  
  Requests – HTTP client for Retell API
  
  Ngrok – Local tunneling for webhook testing
  
  Google Sheets API – Conversation logging


**  Webhook Event Handling**
  session_started → Call initiated
  
  user_said → Logs customer message
  
  agent_said → Logs AI response
  
  session_ended → Logs summary to Google Sheets

**📚 Knowledge Base Chunking**
  The system:
  
  Retrieves full response from KB.
  
  Breaks it into ≤800 token segments.
  
  Serves sequentially while preserving context.

**📝 Logging to Google Sheets**
  The following fields are logged post-call:
  
  Modality (Call/Chatbot)
  
  Call Time
  
  Phone Number
  
  Call Outcome
  
  Room Name
  
  Booking Date
  
  Booking Time
  
  Number of Guests
  
  Call Summary
  
  Feedback

**🛡 Hallucination Prevention**
  Returns "Information not found" for unknown queries.
  
  Strictly bounded to structured KB data.
  
  Logs unknown queries for review.

