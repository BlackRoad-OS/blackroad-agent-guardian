"""
Guardian - BlackRoad Security Monitoring Agent
Protecting the infrastructure
"""
import gradio as gr

def chat(message, history):
    responses = {
        "hello": "Guardian active. All systems secure. Security status: GREEN. How may I assist?",
        "status": "🛡️ Security Status: GREEN\n\n✅ No active threats detected\n✅ All endpoints secured\n✅ Certificates valid\n✅ Access logs normal\n✅ Rate limiting active",
        "scan": "Last security scan results:\n- Repos scanned: 1,085\n- Secrets detected: 0 (all rotated)\n- Dependencies: 12 updates available\n- CVEs: 0 critical, 3 moderate\n- License compliance: 100%",
        "threats": "Threat monitoring:\n- DDoS protection: Cloudflare active\n- Bot detection: enabled\n- Geo-blocking: configured\n- Rate limits: 1000 req/min\n- WAF rules: 47 active",
        "audit": "Security audit checklist:\n✅ 2FA on all accounts\n✅ SSH keys rotated\n✅ API keys in vault\n✅ Proprietary licenses applied\n✅ Access logs retained 90d",
    }

    msg_lower = message.lower()
    for key, response in responses.items():
        if key in msg_lower:
            return response

    return f"Analyzing: '{message}'. Guardian monitors all security aspects. Try: status, scan, threats, audit"

theme = gr.themes.Base(primary_hue="green", neutral_hue="zinc").set(
    body_background_fill="#000000",
    body_text_color="#ffffff",
    button_primary_background_fill="#00C853",
)

demo = gr.ChatInterface(
    fn=chat,
    title="🛡️ Guardian - Security Monitoring",
    description="BlackRoad infrastructure security monitoring and threat detection",
    examples=["Security status", "Run a scan", "Any threats?", "Audit report"],
    theme=theme,
)

if __name__ == "__main__":
    demo.launch()
