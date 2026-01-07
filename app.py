from flask import Flask, Response

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>EviLKeRneL | SQLMap Automation Ecosystem</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
:root{
  --bg:#020b07;
  --glass:rgba(18, 40, 28, 0.60);
  --border:rgba(90,255,180,0.25);
  --accent:#11e87d;
  --text:#39ff70;
  --muted:#9fffcf;
}

*{box-sizing:border-box}

body{
  margin:0;
  background:
    radial-gradient(circle at top, #052012, #020b07 65%),
    repeating-linear-gradient(
      0deg,
      rgba(17,232,125,0.035),
      rgba(17,232,125,0.035) 1px,
      transparent 1px,
      transparent 3px
    );
  color:var(--text);
  font-family:"Segoe UI", monospace;
  line-height:1.6;
}

/* ===== GLASS CARD ===== */
.glass{
  background:var(--glass);
  backdrop-filter: blur(18px) saturate(140%);
  -webkit-backdrop-filter: blur(18px) saturate(140%);
  border:1px solid var(--border);
  border-radius:18px;
  box-shadow:0 0 50px rgba(17,232,125,0.18);
}

/* ===== HEADER ===== */
header{
  min-height:100vh;
  display:flex;
  align-items:center;
  justify-content:center;
  padding:40px 20px;
}

.hero{
  max-width:950px;
  padding:60px;
  text-align:center;
}

.hero h1{
  font-size:52px;
  margin:0;
  color:#aaffd9;
  letter-spacing:3px;
}

.hero p{
  color:var(--muted);
  margin:18px 0 35px;
  font-size:18px;
}

/* ===== BUTTON ===== */
.btn{
  display:inline-block;
  padding:15px 32px;
  margin:8px;
  border-radius:999px;
  background:linear-gradient(135deg,#11e87d,#5affb4);
  color:#02140a;
  font-weight:900;
  text-decoration:none;
  letter-spacing:1px;
  box-shadow:0 0 30px rgba(17,232,125,.55);
  transition:all .25s ease;
  cursor:pointer;
}

.btn:hover{
  transform:translateY(-3px) scale(1.04);
  box-shadow:0 0 55px rgba(17,232,125,.9);
}

/* ===== SECTIONS ===== */
section{
  max-width:1200px;
  margin:0 auto 130px;
  padding:0 22px;
}

h2{
  color:#aaffd9;
  font-size:32px;
  margin-bottom:22px;
  letter-spacing:1px;
}

.subtitle{
  color:#7dffb0;
  margin-bottom:25px;
  max-width:800px;
}

/* ===== GRID ===== */
.grid{
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(260px,1fr));
  gap:26px;
}

.card{
  padding:28px;
}

.card h3{
  margin-top:0;
  color:#7dffb0;
}

.card p{
  color:var(--muted);
  font-size:14px;
}

/* ===== LIST ===== */
ul{
  padding-left:18px;
}

li{
  margin:10px 0;
}

/* ===== FOOTER ===== */
footer{
  padding:40px 20px;
  text-align:center;
  color:#6cffb0;
  border-top:1px solid var(--border);
  background:rgba(0,0,0,0.6);
  font-size:14px;
}

/* ===== SCANLINES ===== */
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
    <p>
      A professional SQLMap automation ecosystem built for serious learners,  
      bug bounty hunters, and security researchers.
    </p>

    <!-- BUTTONS (FORCED REDIRECTS) -->
    <div>
      <a class="btn" href="javascript:void(0)"
         onclick="window.location.href='https://t.me/EviLKeRneLfreeTOOLS'">
        FREE TOOLS
      </a>

      <a class="btn" href="javascript:void(0)"
         onclick="window.location.href='https://t.me/EviLKeRneL_Redirect'">
        JOIN COURSE
      </a>

      <a class="btn" href="javascript:void(0)"
         onclick="window.location.href='https://t.me/EviLKeRneL'">
        CONTACT OWNER
      </a>
    </div>
  </div>
</header>

<section>
  <h2>Why Most SQLMap Users Fail</h2>
  <p class="subtitle">
    Most people blame SQLMap. Professionals fix the workflow.
  </p>

  <div class="grid">
    <div class="card glass"><p>❌ Dirty dorks & repeated targets</p></div>
    <div class="card glass"><p>❌ Manual CLI spam without structure</p></div>
    <div class="card glass"><p>❌ No automation or prioritization</p></div>
    <div class="card glass"><p>❌ No post-exploitation filtering</p></div>
  </div>
</section>

<section>
  <h2>The EviLKeRneL Toolchain</h2>
  <p class="subtitle">
    Each tool is designed to remove friction, reduce mistakes, and increase speed.
  </p>

  <div class="grid">
    <div class="card glass">
      <h3>Dork Tools Suite</h3>
      <p>Splitter, dedupe, sorting, merging, persistent database memory for massive dork lists.</p>
    </div>

    <div class="card glass">
      <h3>SQLMap Column Hunter</h3>
      <p>Automatically detect sensitive columns using keyword intelligence.</p>
    </div>

    <div class="card glass">
      <h3>SQLMap Dumper (GUI)</h3>
      <p>Single & multi-URL dumping with clean, readable output.</p>
    </div>

    <div class="card glass">
      <h3>Rows Filter</h3>
      <p>Sort dumped data by importance, keywords, and value.</p>
    </div>

    <div class="card glass">
      <h3>Combo Filter</h3>
      <p>Analyze, clean, and extract usable credentials efficiently.</p>
    </div>
  </div>
</section>

<section>
  <h2>SQLMap Automation Course</h2>
  <p class="subtitle">
    This is not a command-copying course.  
    This is a **thinking-based exploitation workflow**.
  </p>

  <div class="card glass">
    <ul>
      <li>Beginner → advanced SQLMap workflow</li>
      <li>Automation-first mindset</li>
      <li>Real-world exploitation logic</li>
      <li>GUI-based professional tooling</li>
      <li>Bug bounty & lab-tested methods</li>
    </ul>

    <br>

    <a class="btn" href="javascript:void(0)"
       onclick="window.location.href='https://t.me/EviLKeRneL_Redirect'">
      JOIN COURSE VIA TELEGRAM
    </a>
  </div>
</section>

<section>
  <h2>Free Tools Access</h2>
  <p class="subtitle">
    Start free. Upgrade only when you understand the workflow.
  </p>

  <div class="card glass">
    <p>
      Get access to the free versions of selected tools  
      and build your foundation correctly before scaling.
    </p>

    <br>

    <a class="btn" href="javascript:void(0)"
       onclick="window.location.href='https://t.me/EviLKeRneLfreeTOOLS'">
      ACCESS FREE TOOLS
    </a>
  </div>
</section>

<footer>
  © 2026 EviLKeRneL — Built for automation, not noise  
</footer>

</body>
</html>
"""

@app.route("/")
def index():
    return Response(HTML, mimetype="text/html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
