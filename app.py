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
  font-family: "Segoe UI", monospace;
  overflow-x:hidden;
}

/* ====== GLASS CARD ====== */
.glass{
  background:var(--glass);
  backdrop-filter: blur(18px) saturate(140%);
  -webkit-backdrop-filter: blur(18px) saturate(140%);
  border:1px solid var(--border);
  border-radius:16px;
  box-shadow: 0 0 40px rgba(17,232,125,0.08);
}

/* ====== HEADER ====== */
header{
  min-height:100vh;
  display:flex;
  align-items:center;
  justify-content:center;
  text-align:center;
  padding:40px 20px;
}

.hero{
  max-width:900px;
  padding:50px;
}

.hero h1{
  font-size:48px;
  margin:0;
  color:#aaffd9;
  letter-spacing:2px;
}

.hero p{
  margin:15px 0 30px;
  color:var(--muted);
  font-size:18px;
}

.btn{
  display:inline-block;
  padding:14px 28px;
  background:linear-gradient(135deg, #11e87d, #5affb4);
  color:#02140a;
  font-weight:800;
  text-decoration:none;
  border-radius:999px;
  box-shadow:0 0 25px rgba(17,232,125,0.5);
  transition:all .25s ease;
}

.btn:hover{
  transform:translateY(-2px) scale(1.03);
  box-shadow:0 0 45px rgba(17,232,125,0.9);
}

/* ====== SECTIONS ====== */
section{
  max-width:1100px;
  margin:0 auto 120px;
  padding:0 20px;
}

h2{
  color:#aaffd9;
  margin-bottom:20px;
  font-size:30px;
}

.grid{
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(260px,1fr));
  gap:22px;
}

.card{
  padding:26px;
  transition:transform .25s ease, box-shadow .25s ease;
}

.card:hover{
  transform:translateY(-6px);
  box-shadow:0 0 60px rgba(17,232,125,0.25);
}

.card h3{
  margin-top:0;
  color:#7dffb0;
}

.card p{
  color:var(--muted);
  font-size:14px;
}

/* ====== LIST ====== */
ul{
  padding-left:18px;
}

li{
  margin:8px 0;
}

/* ====== FOOTER ====== */
footer{
  padding:40px 20px;
  text-align:center;
  color:#6cffb0;
  font-size:14px;
  border-top:1px solid var(--border);
  background:rgba(0,0,0,0.5);
}

/* ====== SCANLINE EFFECT ====== */
.scanlines::before{
  content:"";
  position:fixed;
  inset:0;
  background:
    repeating-linear-gradient(
      to bottom,
      rgba(255,255,255,0.02),
      rgba(255,255,255,0.02) 1px,
      transparent 1px,
      transparent 3px
    );
  pointer-events:none;
  z-index:999;
}
</style>
</head>

<body class="scanlines">

<header>
  <div class="hero glass">
    <h1>EviLKeRneL</h1>
    <p>SQLMap Automation • GUI Tools • Workflow over Commands</p>
    <a class="btn" href="#free">ACCESS FREE TOOL</a>
  </div>
</header>

<section>
  <h2>Why Most SQLMap Users Fail</h2>
  <div class="grid">
    <div class="card glass"><p>❌ Dirty dorks & duplicate targets</p></div>
    <div class="card glass"><p>❌ Manual CLI chaos</p></div>
    <div class="card glass"><p>❌ No post-exploitation filtering</p></div>
    <div class="card glass"><p>❌ No automation mindset</p></div>
  </div>
</section>

<section>
  <h2>The EviLKeRneL Ecosystem</h2>
  <div class="grid">
    <div class="card glass">
      <h3>Dork Tools Suite</h3>
      <p>Splitter • Dedupe • Sort • Merge • Persistent DB memory</p>
    </div>
    <div class="card glass">
      <h3>SQLMap Column Hunter</h3>
      <p>Auto-detect sensitive columns with keyword intelligence</p>
    </div>
    <div class="card glass">
      <h3>SQLMap Dumper (GUI)</h3>
      <p>Single & Multi-URL dumping with clean structured output</p>
    </div>
    <div class="card glass">
      <h3>Rows Filter</h3>
      <p>Prioritize valuable dumped data automatically</p>
    </div>
    <div class="card glass">
      <h3>Combo Filter</h3>
      <p>Clean, analyze & extract usable combos fast</p>
    </div>
  </div>
</section>

<section>
  <h2>SQLMap Automation Course</h2>
  <div class="glass card">
    <ul>
      <li>Beginner → Advanced workflow</li>
      <li>Automation-first mindset</li>
      <li>Real-world exploitation logic</li>
      <li>GUI-based professional tooling</li>
    </ul>
    <br>
    <a class="btn" href="https://t.me/EviLKeRneL_Redirect">JOIN VIA TELEGRAM</a>
  </div>
</section>

<section id="free">
  <h2>Free Tool Access</h2>
  <div class="glass card">
    <p>
      Start with the <strong>FREE version</strong> of the Dork Tools Suite.  
      Fix your workflow before running SQLMap.
    </p>
    <br>
    <a class="btn" href="https://t.me/EviLKeRneL_Redirect">GET FREE TOOL</a>
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
