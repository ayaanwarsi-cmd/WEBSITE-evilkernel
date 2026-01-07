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

canvas{position:fixed;inset:0;z-index:-1}

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
 max-width:1200px;
 padding:70px;
 text-align:center;
}

h1{font-size:60px;color:#aaffd9;margin:0}
.tagline{color:#7dffb0;margin-top:10px;font-size:18px}

.terminal{
 background:#000;
 padding:22px;
 border-radius:12px;
 text-align:left;
 margin:35px auto 15px;
 max-width:820px;
}

.btn{
 padding:16px 38px;
 margin:12px;
 border-radius:999px;
 background:linear-gradient(135deg,#11e87d,#5affb4);
 color:#02140a;
 font-weight:900;
 cursor:pointer;
 text-decoration:none;
}

section{
 max-width:1350px;
 margin:0 auto 150px;
 padding:0 26px;
}

h2{font-size:38px;color:#aaffd9}
.subtitle{color:#7dffb0;max-width:950px;margin-bottom:34px}

.grid{
 display:grid;
 grid-template-columns:repeat(auto-fit,minmax(300px,1fr));
 gap:32px;
}

.card{padding:34px}

.badge{
 display:inline-block;
 margin:8px;
 padding:8px 14px;
 border:1px solid var(--border);
 border-radius:8px;
 font-size:13px;
 color:#9fffcf;
}

.counter{color:#ffcc70;font-size:18px;margin-top:10px}

.toast{
 position:fixed;
 bottom:20px;
 left:20px;
 padding:14px 18px;
 font-size:13px;
 display:none;
 z-index:999;
}

footer{
 text-align:center;
 padding:55px;
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
<div class="tagline">Automation over noise • Built for serious operators</div>

<div class="terminal">
<pre>
$ initializing proxy engine...
$ loading sqlmap automation...
$ preparing workflow...
$ all systems ready
</pre>
</div>

<div class="counter">
🔥 Only <span id="seats">17</span> PRO seats left
</div>

<a class="btn" onclick="location.href='https://t.me/EviLKeRneLfreeTOOLS'">FREE TOOLS</a>
<a class="btn" onclick="location.href='https://t.me/EviLKeRneL_Redirect'">JOIN COURSE</a>
<a class="btn" onclick="location.href='https://t.me/EviLKeRneL'">CONTACT OWNER</a>

<div>
<span class="badge">🔒 Secure Access</span>
<span class="badge">⚡ Instant Telegram Access</span>
<span class="badge">🛡️ Trusted by 1000+ Learners</span>
</div>

</div>
</header>

<section>
<h2>Live Global Activity</h2>
<div class="grid">
<div class="card glass">🇮🇳 User from India joined PRO</div>
<div class="card glass">🇩🇪 User from Germany unlocked ELITE</div>
<div class="card glass">🇺🇸 User from USA accessed automation tools</div>
</div>
</section>

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
<div class="card glass"><h3>Before</h3><ul><li>Dead proxies</li><li>Messy dorks</li><li>Guesswork</li></ul></div>
<div class="card glass"><h3>After</h3><ul><li>Live proxies</li><li>Clean workflow</li><li>Automation</li></ul></div>
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
<h2>FAQ</h2>
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

<footer>
© 2026 EviLKeRneL — Built for professionals, not noise
</footer>

<div class="toast glass" id="telegramToast">
Need access? Join Telegram now ⚡
</div>

<script>
// Seats countdown
let seats=17;
setInterval(()=>{
 if(seats>3 && Math.random()>0.7){
  seats--;
  document.getElementById("seats").innerText=seats;
 }
},8000);

// Auto Telegram popup
setTimeout(()=>{
 const t=document.getElementById("telegramToast");
 t.style.display="block";
 t.onclick=()=>location.href='https://t.me/EviLKeRneL_Redirect';
},10000);

// Matrix rain
const c=document.getElementById("matrix"),x=c.getContext("2d");
c.width=innerWidth;c.height=innerHeight;
const letters="01",cols=c.width/20,drops=Array(Math.floor(cols)).fill(1);
setInterval(()=>{
 x.fillStyle="rgba(0,0,0,0.05)";
 x.fillRect(0,0,c.width,c.height);
 x.fillStyle="#11e87d";x.font="16px monospace";
 drops.forEach((y,i)=>{
  x.fillText(letters[Math.random()*2|0],i*20,y*20);
  if(y*20>c.height&&Math.random()>0.975)drops[i]=0;
  drops[i]++;
 });
},50);
</script>

</body>
</html>
"""

@app.route("/")
def index():
 return Response(HTML, mimetype="text/html")

if __name__ == "__main__":
 app.run(host="0.0.0.0", port=5000)
