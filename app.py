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
  --bg:#061108;
  --panel:#0e1c13;
  --accent:#11e87d;
  --text:#39ff70;
  --muted:#0b2918;
}

*{box-sizing:border-box}

body{
  margin:0;
  background:var(--bg);
  color:var(--text);
  font-family:Segoe UI, monospace;
  line-height:1.6;
}

header{
  background:#000;
  padding:60px 20px;
  text-align:center;
  border-bottom:2px solid var(--accent);
}

header h1{
  font-size:42px;
  margin:0;
  color:var(--accent);
}

header p{
  margin:10px 0 20px;
  color:#7dffb0;
}

.btn{
  display:inline-block;
  padding:14px 24px;
  background:var(--accent);
  color:#000;
  font-weight:700;
  text-decoration:none;
  border-radius:4px;
}

section{
  max-width:1000px;
  margin:auto;
  padding:50px 20px;
}

h2{
  color:var(--accent);
  border-left:4px solid var(--accent);
  padding-left:12px;
}

.card{
  background:var(--panel);
  padding:20px;
  margin:20px 0;
  border-left:4px solid var(--accent);
}

.grid{
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
  gap:20px;
}

.bad{
  color:#ff6b6b;
}

.good{
  color:#7dffb0;
}

footer{
  text-align:center;
  padding:20px;
  background:#000;
  border-top:2px solid var(--accent);
  font-size:14px;
}

.highlight{
  background:var(--muted);
  padding:10px;
  border-left:3px solid var(--accent);
  margin:15px 0;
}
</style>
</head>

<body>

<header>
  <h1>EviLKeRneL</h1>
  <p>SQLMap Automation • GUI Tools • Real-World Workflow</p>
  <a class="btn" href="#free">GET FREE TOOL</a>
</header>

<section>
<h2>❌ Why Most SQLMap Users Fail</h2>
<ul>
<li class="bad">Messy dorks & duplicates</li>
<li class="bad">Manual CLI workflows</li>
<li class="bad">Wasted scans & time</li>
<li class="bad">No post-exploitation filtering</li>
</ul>
</section>

<section>
<h2>✅ The EviLKeRneL Solution</h2>
<div class="highlight">
Automation-first SQLMap ecosystem — prepare, exploit, filter, repeat.
</div>
</section>

<section>
<h2>🧰 Tools Included</h2>

<div class="grid">

<div class="card">
<h3>Dork Tools Suite</h3>
<p>Splitter • Line Remover • Dedupe • Sort • Merger • DB-based tracking</p>
</div>

<div class="card">
<h3>SQLMap Column Hunter</h3>
<p>Automatically finds sensitive columns using keywords</p>
</div>

<div class="card">
<h3>SQLMap Dumper (GUI)</h3>
<p>Single & Multi URL dumping with clean readable output</p>
</div>

<div class="card">
<h3>Rows Filter</h3>
<p>Sort dumped data by priority & keywords</p>
</div>

<div class="card">
<h3>Combo Filter</h3>
<p>Analyze & clean combo lists efficiently</p>
</div>

</div>
</section>

<section>
<h2>🎓 SQLMap Automation Course</h2>
<ul class="good">
<li>Beginner → Advanced workflow</li>
<li>Real exploitation demos</li>
<li>GUI-based automation</li>
<li>Bug bounty mindset</li>
</ul>

<div class="highlight">
This course teaches **HOW TO THINK**, not just commands.
</div>

<a class="btn" href="#contact">JOIN COURSE</a>
</section>

<section id="free">
<h2>🆓 Free Tool</h2>
<p>
Start with the **free version** of the Dork Tools Suite and fix your workflow before SQLMap.
</p>
<a class="btn" href="https://t.me/EviLKeRneL">DOWNLOAD FREE TOOL</a>
</section>

<section id="contact">
<h2>📩 Contact & Updates</h2>
<p>Telegram: <strong>@EviLKeRneL</strong></p>
<p>All updates & tools released there.</p>
</section>

<footer>
© 2026 EviLKeRneL — Automation over noise
</footer>

</body>
</html>
"""

@app.route("/")
def index():
    return Response(HTML, mimetype="text/html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
