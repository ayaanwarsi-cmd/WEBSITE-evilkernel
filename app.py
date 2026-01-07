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
  max-width:1050px;
  padding:60px;
  text-align:center;
}

h1{
  font-size:56px;
  color:#aaffd9;
  margin:0;
  letter-spacing:3px;
}

.terminal{
  background:#000;
  padding:18px;
  border-radius:12px;
  text-align:left;
  margin:30px auto 15px;
  max-width:750px;
  box-shadow:0 0 30px rgba(0,255,140,.35);
}

.btn{
  display:inline-block;
  padding:15px 34px;
  margin:10px;
  border-radius:999px;
  background:linear-gradient(135deg,#11e87d,#5affb4);
  color:#02140a;
  font-weight:900;
  border:none;
  cursor:pointer;
  text-decoration:none;
  letter-spacing:1px;
  box-shadow:0 0 35px rgba(17,232,125,.6);
}

section{
  max-width:1250px;
  margin:0 auto 130px;
  padding:0 22px;
}

h2{
  color:#aaffd9;
  font-size:34px;
  margin-bottom:15px;
}

.subtitle{
  color:#7dffb0;
  max-width:850px;
  margin-bottom:30px;
}

.grid{
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(270px,1fr));
  gap:28px;
}

.card{
  padding:30px;
}

.counter{
  margin:10px 0 25px;
  color:#7dffb0;
  font-size:14px;
}

footer{
  text-align:center;
  padding:45px;
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

<div class="terminal">
<pre id="typing"></pre>
</div>

<div class="counter">
👁️ <span id="live">134</span> operators online
</div>

<a class="btn" onclick="location.href='https://t.me/EviLKeRneLfreeTOOLS'">
FREE TOOLS
</a>

<a class="btn" onclick="location.href='https://t.me/EviLKeRneL_Redirect'">
JOIN COURSE
</a>

<a class="btn" onclick="location.href='https://t.me/EviLKeRneL'">
CONTACT OWNER
</a>

</div>
</header>

<section>
<h2>Proxy Automation Toolkit</h2>
<p class="subtitle">
Proxy scraping, checking, and classification — fully automated.  
No more dead lists. No more manual testing.
</p>

<div class="grid">

<div class="card glass">
<h3>Proxy Scraper & Generator</h3>
<p>
Proxy scraping problem ends here.  
Automatically harvest massive proxy lists from dozens of public sources
with deduplication built-in.
</p>
</div>

<div class="card glass">
<h3>High-Speed Proxy Checker</h3>
<p>
Test HTTP, SOCKS4, and SOCKS5 proxies at extreme speed using concurrency.
Dead proxies are removed instantly.
</p>
</div>

<div class="card glass">
<h3>Proxy Classification Engine</h3>
<p>
Automatically classify proxies as <b>Elite</b>, <b>Anonymous</b>, or
<b>Transparent</b> using real IP leakage detection.
</p>
</div>

</div>
</section>

<section>
<h2>SQLMap Automation Ecosystem</h2>
<p class="subtitle">
Designed to eliminate manual SQLMap pain and convert chaos into structure.
</p>

<div class="grid">

<div class="card glass">
<h3>Dork Intelligence Suite</h3>
<p>
Split, dedupe, sort, merge, and permanently track scanned targets.
Your SQLMap success starts here.
</p>
</div>

<div class="card glass">
<h3>SQLMap Column Hunter</h3>
<p>
Automatically locate sensitive columns using keyword intelligence.
No more guessing table structures.
</p>
</div>

<div class="card glass">
<h3>SQLMap Dumper (GUI)</h3>
<p>
Dump databases from single or multiple targets with clean,
human-readable output designed for speed.
</p>
</div>

<div class="card glass">
<h3>Rows & Combo Filters</h3>
<p>
Extract only valuable rows, credentials, and patterns from massive dumps.
Post-exploitation done right.
</p>
</div>

</div>
</section>

<section>
<h2>Why EviLKeRneL?</h2>
<p class="subtitle">
This is not a copy-paste command collection.
This is a professional automation mindset.
</p>

<div class="grid">

<div class="card glass">
<p>✔ Built for real-world workflows</p>
</div>

<div class="card glass">
<p>✔ GUI-driven speed & clarity</p>
</div>

<div class="card glass">
<p>✔ Automation over brute force</p>
</div>

<div class="card glass">
<p>✔ Designed by practitioners</p>
</div>

</div>
</section>

<footer>
© 2026 EviLKeRneL — Automation beats noise
</footer>

<script>
// TERMINAL TYPING
const lines=[
"$ loading proxy intelligence...",
"$ initializing sqlmap automation...",
"$ removing manual bottlenecks...",
"$ workflow ready",
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

// FAKE LIVE USERS
let live=120+Math.floor(Math.random()*40);
setInterval(()=>{
 live+=Math.floor(Math.random()*5-2);
 if(live<80)live=80;
 if(live>260)live=260;
 document.getElementById("live").innerText=live;
},3000);
</script>

</body>
</html>
"""

@app.route("/")
def index():
    return Response(HTML, mimetype="text/html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
