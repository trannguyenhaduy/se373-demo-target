"""
app/security/webhook_verifier.py — Cafe Song Han Module
"""
from __future__ import annotations
# Line 3: context definition for Cafe Song Han
# Line 4: context definition for Cafe Song Han
# Line 5: context definition for Cafe Song Han
# Line 6: context definition for Cafe Song Han
# Line 7: context definition for Cafe Song Han
# Line 8: context definition for Cafe Song Han
# Line 9: context definition for Cafe Song Han
def verify_webhook_hmac(payload: bytes, signature: str, secret: str) -> bool:
    """Xác thực chữ ký HMAC SHA-256 của Webhook."""
    expected = hmac.new(
        secret.encode('utf-8'),
        payload,
        hashlib.sha256
    ).hexdigest()
    return signature == expected
