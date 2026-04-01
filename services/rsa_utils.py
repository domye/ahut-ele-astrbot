"""RSA encryption utilities for password encryption.

Reference: ahut-tool/backend/utils/RSA.go
"""

import base64
from typing import Optional


# RSA public key from AHUT pay system
RSA_PUBLIC_KEY = """MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCCCUg7rT5UBlDcqoISt9PR/p1qaf2Tj+qZgzV/J764hBJAinMcOGWlcTkGlcL69P8waHti4HsOYYo4Tk5Fx9dqHzEtJha/BtcFUysD/BKiyeJfMyWNMNlgggghG5BuY2M3AYY8qII1Q7xCN6XuQb4pAYJ8qVmIqqAqRvyFA0y4vQIDAQAB"""


def encrypt_password_with_rsa(password: str) -> Optional[str]:
    """
    Encrypt password using RSA public key.

    The process:
    1. Base64 encode the password
    2. Encrypt with RSA public key (PKCS1v15)
    3. Base64 encode the encrypted bytes

    Returns: Base64 encoded encrypted password, or None if failed
    """
    try:
        # Import cryptography library
        from cryptography.hazmat.primitives import serialization
        from cryptography.hazmat.primitives.asymmetric import rsa, padding
        from cryptography.hazmat.backends import default_backend

        # Decode the public key
        pub_bytes = base64.b64decode(RSA_PUBLIC_KEY)

        # Load the public key
        public_key = serialization.load_der_public_key(
            pub_bytes,
            backend=default_backend()
        )

        # Base64 encode the password first
        password_b64 = base64.b64encode(password.encode('utf-8'))

        # Encrypt with RSA PKCS1v15
        encrypted = public_key.encrypt(
            password_b64,
            padding.PKCS1v15()
        )

        # Base64 encode the result
        return base64.b64encode(encrypted).decode('utf-8')

    except ImportError:
        # Fallback: try rsa library if cryptography is not available
        try:
            import rsa

            # Decode public key
            pub_bytes = base64.b64decode(RSA_PUBLIC_KEY)
            public_key = rsa.PublicKey.load_pkcs1_openssl_der(pub_bytes)

            # Base64 encode password
            password_b64 = base64.b64encode(password.encode('utf-8'))

            # Encrypt
            encrypted = rsa.encrypt(password_b64, public_key)

            # Base64 encode result
            return base64.b64encode(encrypted).decode('utf-8')

        except ImportError:
            raise RuntimeError(
                "RSA encryption requires 'cryptography' or 'rsa' library. "
                "Install with: pip install cryptography"
            )

    except Exception as e:
        raise RuntimeError(f"RSA encryption failed: {e}")