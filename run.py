# run
from comment_generator import app
 
if __name__ == "__main__":
    # The session object needs a secret key
    app.secret_key = "HopKIdf78/*9*PO72xQ89Fg??"
    app.run()