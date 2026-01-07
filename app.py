from flask import Flask, Response

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>EviLKeRneL | SQLMap Automation</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
:root{
  --bg:#020b07;
  --glass:rgba(18, 40, 28, 0.55);
  --border:rgba(90,255,180,0.25);
  --accent:#11e87d;
  --text:#39ff70;
  --muted:#9fffcf;
}

*{box-sizing:border-box}

body{
  margin:0;
  background:
    radial-gradient(circle at top, #052012, #020b07 60%),
    repeating-linear-gradient(
      0deg,
      rgba(17,232,125,0.04),
      rgba(17,232,125,0.04) 1px,
      transparent 1px,
      transparent 3px
    );
  color:var(--text);
  font-family:Segoe UI, monospace;
}

/* glass */
.glass{
  background:var(--glass);
  backdrop-filter: blur(18px);
  -webkit-backdrop-filter: blur(18px);
  border:1px solid var(--border);
  border-radius:16px;
  box-shadow:0 0 40px rgba(17,232,125,0.15);
}

/* header */
header{
  min-height:100vh;
  display:flex;
  align-items:center;
  justify-content:center;
  padding:40px 20px;
}

.hero{
  max-width:900px;
  padding:50px;
  text-align:center;
}

.hero h1{
  font-size:48px;
  margin:0;
  color:#aaffd9;
}

.hero p{
  color:var(--muted);
  margin:15px 0 30px;
}

.btn{
  display:inline-block;
  padding:14px 30px;
  border-radius:999px;
  background:linear-gradient(135deg,#11e87d,#5affb4);
  color:#02140a;
  font-weight:800;
  text-decoration:none;
  box-shadow:0 0 25px rgba(17,232,125,.5);
}

section{
  max-width:1100px;
  margin:0 auto 120px;
  padding:0 20px;
}

h2{
  color:#aaffd9;
  font-size:30px;
}

.grid{
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(260px,1fr));
  gap:22px;
}

.card{
  padding:26px;
}

footer{
  text-align:center;
  padding:30px;
  color:#6cffb0;
  border-top:1px solid var(--border);
}
</style>
</head>

<body>

<header>
  <div class="hero glass">
    <h1>EviLKeRneL</h1>
    <p>SQLMap Automation • GUI Tools • Workflow over Commands</p>

    <!-- FREE TOOLS BUTTON -->
    <a class="btn" href="https://t.me/EviLKeRneLfreeTOOLS" target="_blank">
      GET FREE TOOLS
    </a>
  </div>
</header>

<section>
  <h2>The EviLKeRneL Ecosystem</h2>
  <div class="grid">
    <div class="card glass"><p>Dork Tools Suite</p></div>
    <div class="card glass"><p>SQLMap Column Hunter</p></div>
    <div class="card glass"><p>SQLMap Dumper (GUI)</p></div>
    <div class="card glass"><p>Rows Filter</p></div>
    <div class="card glass"><p>Combo Filter</p></div>
  </div>
</section>

<section>
  <h2>SQLMap Automation Course</h2>
  <div class="card glass">
    <p>
      Learn the complete SQLMap automation workflow used by professionals.
    </p>
    <br>

    <!-- JOIN COURSE BUTTON -->
    <a class="btn" href="https://t.me/EviLKeRneL_Redirect" target="_blank">
      JOIN COURSE
    </a>
  </div>
</section>

<footer>
  © 2026 EviLKeRneL — Automation beats noise
</footer>

</body>
</html>
"""

@app.route("/")
def index():
    return Response(HTML, mimetype="text/html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
