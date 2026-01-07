from flask import Flask, Response

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>EviLKeRneL | Automation Toolkit</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
:root{
  --bg:#020b07;
  --glass:rgba(18,40,28,.65);
  --border:rgba(90,255,180,.25);
  --accent:#11e87d;
  --text:#39ff70;
  --muted:#9fffcf;
}

*{box-sizing:border-box}

body{
  margin:0;
  background:#020b07;
  color:var(--text);
  font-family:Segoe UI, monospace;
  overflow-x:hidden;
}

/* PAGE LOAD */
body.loaded .hero{
  opacity:1;
  transform:translateY(0);
}
.hero{
  opacity:0;
  transform:translateY(30px);
  transition:all .9s ease;
}

/* MATRIX */
canvas{
  position:fixed;
  inset:0;
  z-index:-1;
}

/* GLASS */
.glass{
  background:var(--glass);
  backdrop-filter:blur(18px);
  border:1px solid var(--border);
  border-radius:18px;
  box-shadow:0 0 40px rgba(17,232,125,.18);
}

/* HEADER */
header{
  min-height:100vh;
  display:flex;
  align-items:center;
  justify-content:center;
  padding:30px 15px;
}

.hero{
  max-width:1100px;
  width:100%;
  padding:50px 25px;
  text-align:center;
}

h1{
  font-size:clamp(38px,6vw,58px);
  color:#aaffd9;
  margin:0;
}

.tagline{
  color:#7dffb0;
  margin-top:8px;
  font-size:clamp(14px,3.5vw,18px);
}

.terminal{
  background:#000;
  padding:18px;
  border-radius:12px;
  text-align:left;
  margin:25px auto;
  max-width:800px;
  font-size:13px;
}

/* CTA */
.cta-row{
  display:flex;
  flex-wrap:wrap;
  justify-content:center;
  gap:14px;
  margin-top:25px;
}

.btn{
  padding:14px 28px;
  border-radius:999px;
  background:linear-gradient(135deg,#11e87d,#5affb4);
  color:#02140a;
  font-weight:900;
  border:none;
  cursor:pointer;
  text-decoration:none;
  font-size:14px;
}

/* BADGES */
.badges{
  display:flex;
  flex-wrap:wrap;
  justify-content:center;
  gap:10px;
  margin-top:16px;
}

.badge{
  padding:7px 14px;
  border:1px solid var(--border);
  border-radius:999px;
  font-size:12px;
  color:#9fffcf;
}

/* SECTIONS */
section{
  max-width:1250px;
  margin:0 auto 100px;
  padding:0 18px;
}

h2{
  font-size:clamp(26px,5vw,36px);
  color:#aaffd9;
  margin-bottom:12px;
  text-align:center;
}

.subtitle{
  color:#7dffb0;
  text-align:center;
  max-width:900px;
  margin:0 auto 30px;
  font-size:14px;
}

.grid{
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(260px,1fr));
  gap:22px;
}

.card{
  padding:26px;
  font-size:14px;
}

.live-box{
  max-width:520px;
  margin:0 auto;
  text-align:center;
  font-size:14px;
}

/* FOOTER */
footer{
  text-align:center;
  padding:40px 15px;
  border-top:1px solid var(--border);
  color:#6cffb0;
  font-size:13px;
}

@media(max-width:600px){
  .terminal{font-size:12px}
  .btn{width:100%; max-width:260px}
}
</style>
</head>

<body>

<canvas id="matrix"></canvas>

<header>
<div class="hero glass">

<h1>EviLKeRneL</h1>
<div class="tagline">Automation over noise • Built for serious operators</div>

<div class="terminal">
<pre>
$ initializing proxy engine...
$ loading sqlmap automation...
$ preparing workflow...
$ all systems ready
</pre>
</div>

<div class="cta-row">
  <a class="btn" onclick="location.href='https://t.me/EviLKeRneLfreeTOOLS'">FREE TOOLS</a>
  <a class="btn" onclick="location.href='https://t.me/EviLKeRneL_Redirect'">JOIN COURSE</a>
  <a class="btn" onclick="location.href='https://t.me/EviLKeRneL'">CONTACT OWNER</a>
</div>

<div class="badges">
  <span class="badge">🔒 Secure Access</span>
  <span class="badge">⚡ Instant Telegram Access</span>
  <span class="badge">🛡️ Trusted by 1000+ Learners</span>
</div>

</div>
</header>

<section>
<h2>What You Will Be Able To Do</h2>
<div class="grid">
  <div class="card glass">Run SQLMap confidently</div>
  <div class="card glass">Handle proxies at scale</div>
  <div class="card glass">Automate repetitive exploitation</div>
  <div class="card glass">Extract only high-value data</div>
</div>
</section>

<section>
<h2>Before vs After</h2>
<div class="grid">
  <div class="card glass">
    <h3>Before</h3>
    <ul>
      <li>Dead proxies</li>
      <li>Messy dorks</li>
      <li>Guesswork</li>
    </ul>
  </div>
  <div class="card glass">
    <h3>After</h3>
    <ul>
      <li>Live proxies</li>
      <li>Clean workflow</li>
      <li>Automation</li>
    </ul>
  </div>
</div>
</section>

<section>
<h2>Instant Access Guarantee</h2>
<div class="grid">
  <div class="card glass">Instant Telegram access</div>
  <div class="card glass">No waiting / approvals</div>
  <div class="card glass">Direct owner support (Elite)</div>
</div>
</section>

<section>
<h2>Frequently Asked Questions</h2>
<div class="grid">
  <div class="card glass">Beginner friendly? → YES</div>
  <div class="card glass">Lifetime access? → YES</div>
  <div class="card glass">Updates included? → YES</div>
  <div class="card glass">Refunds? → Contact owner</div>
</div>
</section>

<section>
<h2>Why I Built This</h2>
<p class="subtitle">
I was tired of broken guides and random workflows.
I built automation for myself first — then shared it with serious learners.
</p>
</section>

<section>
<h2>Roadmap</h2>
<div class="grid">
  <div class="card glass">More proxy sources</div>
  <div class="card glass">Faster checking engine</div>
  <div class="card glass">New automation modules</div>
</div>
</section>

<section>
<h2>Live Global Activity</h2>
<div class="live-box glass" id="geoText">
🇮🇳 User from India joined <b>PRO</b>
</div>
</section>

<footer>
© 2026 EviLKeRneL — Automation beats noise
</footer>

<script>
window.onload = () => document.body.classList.add("loaded");

// MATRIX (OPTIMIZED)
const isMobile = window.innerWidth < 768;
const c = document.getElementById("matrix");
const x = c.getContext("2d");
c.width = innerWidth;
c.height = innerHeight;

const letters = "01";
const fontSize = isMobile ? 18 : 15;
const speed = isMobile ? 90 : 50;
const columns = Math.floor(c.width / (isMobile ? 30 : 20));
const drops = Array(columns).fill(1);

setInterval(()=>{
  x.fillStyle="rgba(0,0,0,0.08)";
  x.fillRect(0,0,c.width,c.height);
  x.font = fontSize + "px monospace";
  drops.forEach((y,i)=>{
    x.fillStyle="#11e87d";
    x.fillText(letters[Math.random()*2|0], i*(isMobile?30:20), y*fontSize);
    if(y*fontSize > c.height && Math.random()>0.97) drops[i]=0;
    drops[i]++;
  });
}, speed);

// CLEAN GEO ACTIVITY — NO COUNTRY CODES
const geoLogs = [
  "🇮🇳 User from India joined PRO",
  "🇩🇪 User from Germany unlocked ELITE",
  "🇺🇸 User from United States accessed automation tools",
  "🇨🇦 User from Canada started automation workflow",
  "🇦🇺 User from Australia joined PRO"
];

let gi = 0;
setInterval(()=>{
  document.getElementById("geoText").innerHTML = geoLogs[gi];
  gi = (gi + 1) % geoLogs.length;
}, 3500);
</script>

</body>
</html>
"""

@app.route("/")
def index():
    return Response(HTML, mimetype="text/html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
