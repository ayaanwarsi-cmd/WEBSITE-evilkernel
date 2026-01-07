from flask import Flask, Response

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>EviLKeRneL | Professional Automation Toolkit</title>
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

canvas{
  position:fixed;
  inset:0;
  z-index:-1;
}

.glass{
  background:var(--glass);
  backdrop-filter:blur(18px);
  border:1px solid var(--border);
  border-radius:18px;
  box-shadow:0 0 50px rgba(17,232,125,.18);
}

header{
  min-height:100vh;
  display:flex;
  align-items:center;
  justify-content:center;
  padding:40px 20px;
}

.hero{
  max-width:1100px;
  padding:65px;
  text-align:center;
}

h1{
  font-size:58px;
  color:#aaffd9;
  margin:0;
  letter-spacing:3px;
}

.tagline{
  margin-top:10px;
  color:#7dffb0;
  font-size:18px;
}

.terminal{
  background:#000;
  padding:20px;
  border-radius:12px;
  text-align:left;
  margin:35px auto 15px;
  max-width:780px;
  box-shadow:0 0 35px rgba(0,255,140,.4);
}

.btn{
  display:inline-block;
  padding:15px 36px;
  margin:12px;
  border-radius:999px;
  background:linear-gradient(135deg,#11e87d,#5affb4);
  color:#02140a;
  font-weight:900;
  cursor:pointer;
  text-decoration:none;
  letter-spacing:1px;
  box-shadow:0 0 35px rgba(17,232,125,.6);
}

section{
  max-width:1300px;
  margin:0 auto 140px;
  padding:0 24px;
}

h2{
  color:#aaffd9;
  font-size:36px;
  margin-bottom:16px;
}

.subtitle{
  color:#7dffb0;
  max-width:900px;
  margin-bottom:32px;
}

.grid{
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(280px,1fr));
  gap:30px;
}

.card{
  padding:32px;
}

.counter{
  margin-top:10px;
  font-size:14px;
  color:#7dffb0;
}

.activity{
  margin-top:15px;
  font-size:13px;
  color:#9fffcf;
}

footer{
  text-align:center;
  padding:50px;
  border-top:1px solid var(--border);
  color:#6cffb0;
}
</style>
</head>

<body>

<canvas id="matrix"></canvas>

<header>
<div class="hero glass">

<h1>EviLKeRneL</h1>
<div class="tagline">Automation over noise • Tools built for real operators</div>

<div class="terminal">
<pre id="typing"></pre>
</div>

<div class="counter">
👁️ <span id="live">138</span> operators online
</div>

<div class="activity" id="activity"></div>

<a class="btn" onclick="location.href='https://t.me/EviLKeRneLfreeTOOLS'">FREE TOOLS</a>
<a class="btn" onclick="location.href='https://t.me/EviLKeRneL_Redirect'">JOIN COURSE</a>
<a class="btn" onclick="location.href='https://t.me/EviLKeRneL'">CONTACT OWNER</a>

</div>
</header>

<section>
<h2>Proxy Automation Toolkit</h2>
<p class="subtitle">
Proxy scraping problem ends here. Generate, check, filter and classify proxies
at massive scale without manual testing.
</p>

<div class="grid">
<div class="card glass">
<h3>Proxy Scraper & Generator</h3>
<p>
Collect millions of HTTP, SOCKS4 and SOCKS5 proxies from public sources.
Automatic deduplication and formatting included.
</p>
</div>

<div class="card glass">
<h3>High Speed Proxy Checker</h3>
<p>
Concurrent proxy checking engine removes dead proxies instantly
and keeps only working endpoints.
</p>
</div>

<div class="card glass">
<h3>Proxy Classification</h3>
<p>
Detect IP leakage and classify proxies as Elite, Anonymous or Transparent
using real request analysis.
</p>
</div>
</div>
</section>

<section>
<h2>SQLMap Automation Ecosystem</h2>
<p class="subtitle">
Built to remove chaos from SQLMap usage and replace it with a structured,
repeatable exploitation workflow.
</p>

<div class="grid">
<div class="card glass">
<h3>Dork Intelligence Suite</h3>
<p>
Split huge dork files, remove duplicates, sort targets and track already
scanned URLs permanently.
</p>
</div>

<div class="card glass">
<h3>SQLMap Column Hunter</h3>
<p>
Automatically identify sensitive database columns using keyword intelligence
without manual inspection.
</p>
</div>

<div class="card glass">
<h3>SQLMap Dumper GUI</h3>
<p>
Dump databases from single or multiple targets with clean,
human-readable output designed for speed.
</p>
</div>

<div class="card glass">
<h3>Rows & Combo Filters</h3>
<p>
Extract only high-value data from massive dumps and combo lists.
Post-exploitation done properly.
</p>
</div>
</div>
</section>

<section>
<h2>Pricing Plans</h2>
<p class="subtitle">Start free. Upgrade when you are ready.</p>

<div class="grid">
<div class="card glass">
<h3>FREE</h3>
<p>$0</p>
<ul>
<li>Limited tools</li>
<li>Basic workflow access</li>
<li>Community support</li>
</ul>
</div>

<div class="card glass">
<h3>PRO</h3>
<p>$35</p>
<ul>
<li>All tools unlocked</li>
<li>Automation workflows</li>
<li>Full course access</li>
</ul>
</div>

<div class="card glass">
<h3>ELITE</h3>
<p>$65</p>
<ul>
<li>Everything in PRO</li>
<li>Priority updates</li>
<li>Direct owner support</li>
</ul>
</div>
</div>
</section>

<footer>
© 2026 EviLKeRneL — Built for professionals, not script-kiddies
</footer>

<script>
// TERMINAL TYPING
const lines=[
"$ initializing proxy engine...",
"$ loading sqlmap automation modules...",
"$ preparing workflow...",
"$ all systems ready",
"$ welcome to EviLKeRneL"
];
let i=0,j=0;
function type(){
 if(i<lines.length){
  if(j<lines[i].length){
   document.getElementById("typing").innerHTML+=lines[i][j++];
   setTimeout(type,40);
  }else{
   document.getElementById("typing").innerHTML+="\\n";
   i++;j=0;setTimeout(type,400);
  }
 }
}
type();

// MATRIX RAIN
const c=document.getElementById("matrix");
const x=c.getContext("2d");
c.width=innerWidth;c.height=innerHeight;
const letters="01";
const cols=c.width/20;
const drops=Array(Math.floor(cols)).fill(1);
setInterval(()=>{
 x.fillStyle="rgba(0,0,0,0.05)";
 x.fillRect(0,0,c.width,c.height);
 x.fillStyle="#11e87d";
 x.font="16px monospace";
 drops.forEach((y,i)=>{
  const t=letters[Math.random()*letters.length|0];
  x.fillText(t,i*20,y*20);
  if(y*20>c.height&&Math.random()>0.975)drops[i]=0;
  drops[i]++;
 });
},50);

// LIVE USERS
let live=120+Math.floor(Math.random()*40);
setInterval(()=>{
 live+=Math.floor(Math.random()*5-2);
 if(live<90)live=90;
 if(live>300)live=300;
 document.getElementById("live").innerText=live;
},3000);

// FAKE PURCHASE FEED
const purchases=[
"User purchased PRO ($35)",
"User upgraded to ELITE ($65)",
"New PRO access activated",
"ELITE plan unlocked",
"PRO plan purchased"
];
setInterval(()=>{
 document.getElementById("activity").innerText =
 "[LIVE] " + purchases[Math.floor(Math.random()*purchases.length)];
},3500);
</script>

</body>
</html>
"""

@app.route("/")
def index():
    return Response(HTML, mimetype="text/html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
