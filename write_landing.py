content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>FarmPrice - Smart Crop Pricing for Indian Farmers</title>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=Nunito:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: 'Nunito', sans-serif; background: #fefae0; color: #1b2b1e; min-height: 100vh; }
.lang-btn { color: white; border: 1px solid #444; padding: 0.3rem 0.7rem; border-radius: 6px; cursor: pointer; font-weight: 700; font-size: 0.85rem; font-family: 'Nunito', sans-serif; transition: all 0.2s; background: transparent; }
.lang-btn.active { background: #2d6a4f; }
@keyframes fadeInUp { from { opacity: 0; transform: translateY(30px); } to { opacity: 1; transform: translateY(0); } }
@keyframes float { 0%,100% { transform: translateY(0); } 50% { transform: translateY(-12px); } }
.fade1 { animation: fadeInUp 0.7s ease forwards; }
.fade2 { animation: fadeInUp 0.7s ease 0.2s forwards; opacity: 0; }
.fade3 { animation: fadeInUp 0.7s ease 0.4s forwards; opacity: 0; }
.fade4 { animation: fadeInUp 0.7s ease 0.6s forwards; opacity: 0; }
.float { animation: float 3s ease-in-out infinite; }
.btn { display: inline-block; padding: 0.8rem 2rem; border-radius: 12px; font-weight: 700; font-size: 1rem; text-decoration: none; border: none; cursor: pointer; transition: all 0.2s; font-family: 'Nunito', sans-serif; }
.btn-gold { background: #f4a261; color: #1b2b1e; }
.btn-gold:hover { background: #e08c47; transform: translateY(-2px); }
.btn-outline { background: transparent; border: 2px solid #52b788; color: #52b788; }
.btn-outline:hover { background: #52b788; color: white; transform: translateY(-2px); }
.feature-card { background: white; border-radius: 16px; padding: 1.75rem; box-shadow: 0 4px 20px rgba(45,106,79,0.1); border: 1px solid #e8f5e9; transition: all 0.3s; }
.feature-card:hover { transform: translateY(-5px); }
@media (max-width: 768px) {
    .hero-title { font-size: 2.2rem !important; }
    .hero-btns { flex-direction: column; }
    .features-grid { grid-template-columns: 1fr !important; }
    .stats-grid { grid-template-columns: repeat(2, 1fr) !important; }
    .hero-card { display: none; }
    .nav-links-desktop { display: none !important; }
}
</style>
</head>
<body>
<nav style="background: #1b2b1e; padding: 0 2rem; display: flex; align-items: center; justify-content: space-between; position: sticky; top: 0; z-index: 100; box-shadow: 0 2px 20px rgba(0,0,0,0.3); min-height: 65px;">
    <a href="/" style="font-family: 'Syne', sans-serif; font-weight: 800; font-size: 1.6rem; color: #52b788; text-decoration: none;">&#127807; Farm<span style="color:#f4a261;">Price</span></a>
    <div style="display:flex; align-items:center; gap:1rem;">
        <div style="display:flex;align-items:center;gap:0.4rem;">
            <button class="lang-btn active" data-lang="en" onclick="switchLang('en')">EN</button>
            <button class="lang-btn" data-lang="hi" onclick="switchLang('hi')">&#2361;&#2367;</button>
            <button class="lang-btn" data-lang="te" onclick="switchLang('te')">&#3108;&#3142;</button>
        </div>
        <div class="nav-links-desktop" style="display:flex; gap:0.75rem;">
            <a href="/login/" style="color:#ccc; text-decoration:none; padding:0.5rem 1rem; border-radius:8px; font-weight:600; font-size:0.9rem;" data-i18n="Login">Login</a>
            <a href="/register/" style="background:#f4a261; color:#1b2b1e; text-decoration:none; padding:0.5rem 1.25rem; border-radius:20px; font-weight:700; font-size:0.9rem;" data-i18n="Register">Register</a>
        </div>
    </div>
</nav>
<section style="background: linear-gradient(135deg, #1b2b1e 0%, #2d6a4f 60%, #52b788 100%); padding: 6rem 0 5rem; position: relative; overflow: hidden;">
    <div style="position:absolute;top:-80px;right:-80px;width:350px;height:350px;border-radius:50%;background:rgba(82,183,136,0.1);"></div>
    <div style="max-width:1200px; margin:0 auto; padding:0 2rem; display:flex; align-items:center; justify-content:space-between; gap:2rem; flex-wrap:wrap; position:relative;">
        <div style="max-width:600px;">
            <div class="fade1" style="background:rgba(244,162,97,0.15);display:inline-block;padding:0.5rem 1.25rem;border-radius:25px;color:#f4a261;font-weight:700;font-size:0.9rem;margin-bottom:1.5rem;border:1px solid rgba(244,162,97,0.3);" data-i18n="tagline_badge">&#128640; Smart Farming for Better Profits</div>
            <h1 class="fade2 hero-title" style="font-family:'Syne',sans-serif;font-size:3.2rem;font-weight:800;color:white;line-height:1.2;margin-bottom:1.5rem;">
                <span data-i18n="hero_line1">Know When to</span><br>
                <span style="color:#52b788;" data-i18n="hero_line2">Sell Your Crops</span><br>
                <span data-i18n="hero_line3">for Maximum Profit</span>
            </h1>
            <p class="fade3" style="color:#b2dfdb;font-size:1.1rem;margin-bottom:2.5rem;line-height:1.8;" data-i18n="hero_desc">AI-powered price predictions, real-time market data, and weather-based sell recommendations — all in one place for Indian farmers.</p>
            <div class="fade4 hero-btns" style="display:flex;gap:1rem;flex-wrap:wrap;">
                <a href="/register/" class="btn btn-gold" data-i18n="get_started">&#127807; Get Started Free</a>
                <a href="/login/" class="btn btn-outline" data-i18n="Login">Login</a>
            </div>
        </div>
        <div class="float hero-card" style="background:rgba(255,255,255,0.1);backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,0.2);border-radius:20px;padding:1.75rem;min-width:230px;text-align:center;">
            <div style="font-size:3rem;margin-bottom:0.75rem;">&#127807;</div>
            <div style="color:#52b788;font-weight:700;font-size:0.8rem;text-transform:uppercase;letter-spacing:0.05em;margin-bottom:0.75rem;" data-i18n="top_price">Today's Top Price</div>
            <div style="font-family:'Syne',sans-serif;font-size:2.2rem;font-weight:800;color:white;">&#8377;2,900</div>
            <div style="color:#b2dfdb;font-size:0.85rem;margin-bottom:1rem;" data-i18n="rice_hyd">Rice - Hyderabad</div>
            <div style="background:rgba(40,167,69,0.2);color:#52b788;padding:0.3rem 0.75rem;border-radius:20px;font-size:0.8rem;font-weight:700;display:inline-block;" data-i18n="trending_up">Trending Up</div>
        </div>
    </div>
</section>
<div style="background:white;border-bottom:1px solid #e8f5e9;padding:2rem 0;">
    <div style="max-width:1200px;margin:0 auto;padding:0 2rem;">
        <div class="stats-grid" style="display:grid;grid-template-columns:repeat(4,1fr);gap:1rem;text-align:center;">
            <div><div style="font-family:'Syne',sans-serif;font-size:2rem;font-weight:800;color:#2d6a4f;">500+</div><div style="color:#6c757d;font-size:0.9rem;font-weight:600;" data-i18n="mandis_tracked">Mandis Tracked</div></div>
            <div><div style="font-family:'Syne',sans-serif;font-size:2rem;font-weight:800;color:#2d6a4f;">50+</div><div style="color:#6c757d;font-size:0.9rem;font-weight:600;" data-i18n="crop_varieties">Crop Varieties</div></div>
            <div><div style="font-family:'Syne',sans-serif;font-size:2rem;font-weight:800;color:#2d6a4f;">10K+</div><div style="color:#6c757d;font-size:0.9rem;font-weight:600;" data-i18n="farmers_helped">Farmers Helped</div></div>
            <div><div style="font-family:'Syne',sans-serif;font-size:2rem;font-weight:800;color:#2d6a4f;">93%</div><div style="color:#6c757d;font-size:0.9rem;font-weight:600;" data-i18n="prediction_accuracy">Prediction Accuracy</div></div>
        </div>
    </div>
</div>
<section style="padding:4rem 0;background:#f8fffe;">
    <div style="max-width:1200px;margin:0 auto;padding:0 2rem;">
        <div style="text-align:center;margin-bottom:3rem;">
            <h2 style="font-family:'Syne',sans-serif;font-size:2rem;font-weight:800;color:#1b2b1e;margin-bottom:0.5rem;" data-i18n="how_helps">How FarmPrice Helps You</h2>
            <p style="color:#6c757d;font-size:1.05rem;" data-i18n="powerful_tools">Powerful tools designed for Indian farmers</p>
        </div>
        <div class="features-grid" style="display:grid;grid-template-columns:repeat(3,1fr);gap:1.5rem;">
            <div class="feature-card">
                <div style="width:60px;height:60px;background:#d8f3dc;border-radius:50%;display:flex;align-items:center;justify-content:center;margin-bottom:1rem;font-size:1.75rem;">&#128202;</div>
                <h3 style="font-family:'Syne',sans-serif;font-weight:700;margin-bottom:0.5rem;" data-i18n="price_pred">Price Prediction</h3>
                <p style="color:#6c757d;line-height:1.7;font-size:0.95rem;" data-i18n="price_pred_desc">AI-powered forecasts for next 15 days. Know if prices will rise or fall before making decisions.</p>
            </div>
            <div class="feature-card" style="border:2px solid #2d6a4f;">
                <div style="width:60px;height:60px;background:#d8f3dc;border-radius:50%;display:flex;align-items:center;justify-content:center;margin-bottom:1rem;font-size:1.75rem;">&#127780;</div>
                <h3 style="font-family:'Syne',sans-serif;font-weight:700;margin-bottom:0.5rem;" data-i18n="weather_advice">Weather-Smart Advice</h3>
                <p style="color:#6c757d;line-height:1.7;font-size:0.95rem;" data-i18n="weather_desc">Get personalized advice on when to harvest and sell based on your local weather forecast.</p>
            </div>
            <div class="feature-card">
                <div style="width:60px;height:60px;background:#d8f3dc;border-radius:50%;display:flex;align-items:center;justify-content:center;margin-bottom:1rem;font-size:1.75rem;">&#128722;</div>
                <h3 style="font-family:'Syne',sans-serif;font-weight:700;margin-bottom:0.5rem;" data-i18n="marketplace">Marketplace</h3>
                <p style="color:#6c757d;line-height:1.7;font-size:0.95rem;" data-i18n="market_desc">List your crops and connect directly with buyers. No middlemen, better prices for your produce.</p>
            </div>
        </div>
    </div>
</section>
<section style="background:linear-gradient(135deg,#2d6a4f,#1b2b1e);padding:4rem 0;text-align:center;">
    <div style="max-width:1200px;margin:0 auto;padding:0 2rem;">
        <h2 style="font-family:'Syne',sans-serif;font-size:2rem;font-weight:800;color:white;margin-bottom:1rem;" data-i18n="ready">Ready to Get Better Prices?</h2>
        <p style="color:#b2dfdb;font-size:1rem;margin-bottom:2rem;" data-i18n="join_farmers">Join thousands of farmers already using FarmPrice</p>
        <a href="/register/" class="btn btn-gold" style="font-size:1.1rem;padding:0.9rem 2.5rem;" data-i18n="get_started">&#127807; Get Started Free</a>
    </div>
</section>
<footer style="background:#1b2b1e;color:#aaa;text-align:center;padding:1.5rem;">
    <p>&#127807; <strong style="color:#52b788;">FarmPrice</strong> — <span data-i18n="footer_tagline">Empowering Indian Farmers with Smart Pricing Intelligence</span></p>
</footer>
<script>
const translations = {
    en: {'Login':'Login','Register':'Register','tagline_badge':'Smart Farming for Better Profits','hero_line1':'Know When to','hero_line2':'Sell Your Crops','hero_line3':'for Maximum Profit','hero_desc':'AI-powered price predictions, real-time market data — all in one place for Indian farmers.','get_started':'Get Started Free','top_price':"Today's Top Price",'rice_hyd':'Rice - Hyderabad','trending_up':'Trending Up','mandis_tracked':'Mandis Tracked','crop_varieties':'Crop Varieties','farmers_helped':'Farmers Helped','prediction_accuracy':'Prediction Accuracy','how_helps':'How FarmPrice Helps You','powerful_tools':'Powerful tools designed for Indian farmers','price_pred':'Price Prediction','price_pred_desc':'AI-powered forecasts for next 15 days.','weather_advice':'Weather-Smart Advice','weather_desc':'Get personalized advice based on your local weather.','marketplace':'Marketplace','market_desc':'List crops and connect with buyers directly.','ready':'Ready to Get Better Prices?','join_farmers':'Join thousands of farmers already using FarmPrice','footer_tagline':'Empowering Indian Farmers with Smart Pricing Intelligence'},
    hi: {'Login':'&#2354;&#2377;&#2327; &#2311;&#2344;','Register':'&#2346;&#2306;&#2332;&#2368;&#2325;&#2352;&#2339;','tagline_badge':'&#2348;&#2375;&#2361;&#2340;&#2352; &#2350;&#2369;&#2344;&#2366;&#2347;&#2375; &#2325;&#2375; &#2354;&#2367;&#2319; &#2360;&#2381;&#2350;&#2366;&#2352;&#2381;&#2335; &#2326;&#2375;&#2340;&#2368;','hero_line1':'&#2332;&#2366;&#2344;&#2375;&#2306; &#2325;&#2348; &#2348;&#2375;&#2330;&#2375;&#2306;','hero_line2':'&#2309;&#2346;&#2344;&#2368; &#2347;&#2360;&#2354;','hero_line3':'&#2309;&#2343;&#2367;&#2325;&#2340;&#2350; &#2354;&#2366;&#2349; &#2325;&#2375; &#2354;&#2367;&#2319;','hero_desc':'AI &#2350;&#2370;&#2354;&#2381;&#2351; &#2346;&#2370;&#2352;&#2381;&#2357;&#2366;&#2344;&#2369;&#2350;&#2366;&#2344; &#2324;&#2352; &#2350;&#2306;&#2337;&#2368; &#2337;&#2375;&#2335;&#2366; &#2349;&#2366;&#2352;&#2340;&#2368;&#2351; &#2325;&#2367;&#2360;&#2366;&#2344;&#2379;&#2306; &#2325;&#2375; &#2354;&#2367;&#2319;','get_started':'&#2350;&#2369;&#2347;&#2381;&#2340; &#2358;&#2369;&#2352;&#2370; &#2325;&#2352;&#2375;&#2306;','top_price':'&#2310;&#2332; &#2325;&#2368; &#2360;&#2348;&#2360;&#2375; &#2309;&#2330;&#2381;&#2331;&#2368; &#2325;&#2368;&#2350;&#2340;','rice_hyd':'&#2330;&#2366;&#2357;&#2354; - &#2361;&#2376;&#2342;&#2352;&#2366;&#2348;&#2366;&#2342;','trending_up':'&#2348;&#2397; &#2352;&#2361;&#2366; &#2361;&#2376;','mandis_tracked':'&#2350;&#2306;&#2337;&#2367;&#2351;&#2366;&#2306; &#2335;&#2381;&#2352;&#2376;&#2325;','crop_varieties':'&#2347;&#2360;&#2354; &#2325;&#2368; &#2325;&#2367;&#2360;&#2381;&#2350;&#2375;&#2306;','farmers_helped':'&#2325;&#2367;&#2360;&#2366;&#2344;&#2379;&#2306; &#2325;&#2368; &#2350;&#2342;&#2342;','prediction_accuracy':'&#2346;&#2370;&#2352;&#2381;&#2357;&#2366;&#2344;&#2369;&#2350;&#2366;&#2344; &#2360;&#2335;&#2368;&#2325;&#2340;&#2366;','how_helps':'FarmPrice &#2325;&#2376;&#2360;&#2375; &#2350;&#2342;&#2342; &#2325;&#2352;&#2340;&#2366; &#2361;&#2376;','powerful_tools':'&#2349;&#2366;&#2352;&#2340;&#2368;&#2351; &#2325;&#2367;&#2360;&#2366;&#2344;&#2379;&#2306; &#2325;&#2375; &#2354;&#2367;&#2319; &#2358;&#2325;&#2381;&#2340;&#2367;&#2358;&#2366;&#2354;&#2368; &#2313;&#2346;&#2325;&#2352;&#2339;','price_pred':'&#2350;&#2370;&#2354;&#2381;&#2351; &#2346;&#2370;&#2352;&#2381;&#2357;&#2366;&#2344;&#2369;&#2350;&#2366;&#2344;','price_pred_desc':'&#2309;&#2327;&#2354;&#2375; 15 &#2342;&#2367;&#2344;&#2379;&#2306; &#2325;&#2375; &#2354;&#2367;&#2319; AI &#2346;&#2370;&#2352;&#2381;&#2357;&#2366;&#2344;&#2369;&#2350;&#2366;&#2344;','weather_advice':'&#2350;&#2380;&#2360;&#2350; &#2360;&#2354;&#2366;&#2361;','weather_desc':'&#2360;&#2381;&#2341;&#2366;&#2344;&#2368;&#2351; &#2350;&#2380;&#2360;&#2350; &#2346;&#2352; &#2310;&#2343;&#2366;&#2352;&#2367;&#2340; &#2360;&#2354;&#2366;&#2361;','marketplace':'&#2348;&#2366;&#2364;&#2366;&#2352;','market_desc':'&#2347;&#2360;&#2354; &#2360;&#2370;&#2330;&#2368;&#2348;&#2342;&#2381;&#2343; &#2325;&#2352;&#2375;&#2306; &#2324;&#2352; &#2326;&#2352;&#2368;&#2342;&#2366;&#2352;&#2379;&#2306; &#2360;&#2375; &#2360;&#2368;&#2343;&#2375; &#2332;&#2369;&#2337;&#2375;&#2306;','ready':'&#2348;&#2375;&#2361;&#2340;&#2352; &#2325;&#2368;&#2350;&#2340; &#2346;&#2366;&#2344;&#2375; &#2325;&#2375; &#2354;&#2367;&#2319; &#2340;&#2376;&#2351;&#2366;&#2352; &#2361;&#2376;&#2306;?','join_farmers':'&#2361;&#2332;&#2366;&#2352;&#2379;&#2306; &#2325;&#2367;&#2360;&#2366;&#2344; FarmPrice &#2313;&#2346;&#2351;&#2379;&#2327; &#2325;&#2352; &#2352;&#2361;&#2375; &#2361;&#2376;&#2306;','footer_tagline':'&#2360;&#2381;&#2350;&#2366;&#2352;&#2381;&#2335; &#2350;&#2370;&#2354;&#2381;&#2351; &#2360;&#2375; &#2349;&#2366;&#2352;&#2340;&#2368;&#2351; &#2325;&#2367;&#2360;&#2366;&#2344;&#2379;&#2306; &#2325;&#2379; &#2360;&#2358;&#2325;&#2381;&#2340; &#2348;&#2344;&#2366;&#2344;&#2366;'},
    te: {'Login':'&#3122;&#3134;&#3095;&#3135;&#3116;&#3149;','Register':'&#3112;&#3118;&#3147;&#3078;&#3137; &#3127;&#3143;&#3119;&#3074;&#3068;&#3135;','tagline_badge':'&#3121;&#3143;&#3120;&#3137;&#3095;&#3132;&#3108;&#3135; &#3122;&#3134;&#3092;&#3134;&#3122;&#3074; &#3056;&#3147;&#3108;&#3118;&#3149; &#3125;&#3149;&#3119;&#3134;&#3120;&#3149;&#3110;&#3074;','hero_line1':'&#3143;&#3114;&#3149;&#3114;&#3137;&#3078;&#3137; &#3105;&#3118;&#3149;&#3118;&#3134;&#3122;&#3147; &#3108;&#3143;&#3122;&#3137;&#3128;&#3137;&#3056;&#3074;&#3068;&#3135;','hero_line2':'&#3121;&#3105;&#3149; &#3114;&#3074;&#3103;&#3122;&#3137; &#3105;&#3118;&#3149;&#3118;&#3074;&#3068;&#3135;','hero_line3':'&#3095;&#3120;&#3135;&#3123;&#3149;&#3103; &#3122;&#3134;&#3092;&#3074; &#3056;&#3147;&#3128;&#3074;','hero_desc':'AI &#3078;&#3120; &#3105;&#3074;&#3127;&#3112;&#3134;&#3122;&#3137; &#3092;&#3074;&#3068;&#3135; &#3121;&#3134;&#3120;&#3149;&#3056;&#3143;&#3103;&#3149; &#3078;&#3134;&#3103;&#3134; &#3092;&#3074;&#3103;&#3149;','get_started':'&#3125;&#3127;&#3111;&#3074;&#3095;&#3074;&#3095;&#3134; &#3114;&#3149;&#3120;&#3134;&#3120;&#3074;&#3091;&#3135;&#3074;&#3127;&#3074;&#3068;&#3135;','top_price':'&#3113;&#3120;&#3149;&#3103;&#3137;&#3078;&#3134; &#3105;&#3108;&#3149;&#3119;&#3137;&#3108;&#3149;&#3108;&#3118; &#3078;&#3120;','rice_hyd':'&#3125;&#3120;&#3135; - &#3112;&#3136;&#3078;&#3122;&#3134;&#3092;&#3134;&#3078;&#3149;','trending_up':'&#3114;&#3143;&#3120;&#3137;&#3095;&#3137;&#3108;&#3147;&#3074;&#3068;&#3135;','mandis_tracked':'&#3121;&#3074;&#3078;&#3105;&#3122;&#3137; &#3103;&#3149;&#3120;&#3134;&#3056;&#3149;','crop_varieties':'&#3114;&#3074;&#3103; &#3120;&#3056;&#3134;&#3122;&#3137;','farmers_helped':'&#3120;&#3136;&#3108;&#3137;&#3122;&#3056;&#3137; &#3128;&#3112;&#3134;&#3119;&#3074;','prediction_accuracy':'&#3105;&#3074;&#3127;&#3112;&#3134;&#3112;&#3122;&#3149; &#3078;&#3127;&#3127;&#3135;&#3108;&#3108;&#3149;&#3125;&#3074;','how_helps':'FarmPrice &#3121;&#3149;&#3056;&#3137; &#3143;&#3122;&#3134; &#3128;&#3112;&#3134;&#3119;&#3134;&#3114;&#3078;&#3135;','powerful_tools':'&#3092;&#3134;&#3120;&#3108; &#3120;&#3136;&#3108;&#3137;&#3122;&#3056;&#3137; &#3056;&#3147;&#3128;&#3074; &#3123;&#3056;&#3149;&#3108;&#3135;&#3125;&#3074;&#3108;&#3118;&#3136;&#3112; &#3128;&#3134;&#3078;&#3112;&#3134;&#3122;&#3137;','price_pred':'&#3078;&#3120; &#3105;&#3074;&#3127;&#3112;&#3134;','price_pred_desc':'15 &#3120;&#3147;&#3091;&#3122;&#3106;&#3137; AI &#3105;&#3074;&#3127;&#3112;&#3134;&#3122;&#3137;','weather_advice':'&#3125;&#3134;&#3108;&#3134;&#3125;&#3120;&#3139;&#3116;&#3074; &#3128;&#3122;&#3112;&#3134;','weather_desc':'&#3128;&#3149;&#3039;&#3134;&#3112;&#3122;&#3149; &#3125;&#3134;&#3108;&#3134;&#3125;&#3120;&#3139;&#3116;&#3074; &#3105;&#3134;&#3078;&#3106;&#3074;&#3095;&#3134; &#3128;&#3122;&#3112;&#3134;','marketplace':'&#3121;&#3134;&#3120;&#3149;&#3056;&#3143;&#3103;&#3149;&#3114;&#3149;&#3122;&#3143;&#3128;&#3149;','market_desc':'&#3121;&#3105;&#3149; &#3114;&#3074;&#3103;&#3112;&#3137; &#3091;&#3134;&#3092;&#3134;&#3103;&#3134; &#3127;&#3143;&#3119;&#3074;&#3068;&#3135;','ready':'&#3121;&#3074;&#3127;&#3135; &#3078;&#3120;&#3122;&#3137; &#3114;&#3147;&#3074;&#3078;&#3108;&#3134;&#3119;&#3135;&#3056;&#3136; &#3128;&#3135;&#3078;&#3149;&#3078;&#3074;&#3095;&#3134; &#3125;&#3137;&#3112;&#3149;&#3112;&#3134;&#3120;&#3134;?','join_farmers':'&#3125;&#3143;&#3122;&#3134;&#3078;&#3135; &#3120;&#3136;&#3108;&#3137;&#3122;&#3137; FarmPrice &#3125;&#3112;&#3095;&#3134;&#3110;&#3135;&#3056;&#3149;&#3108;&#3137;&#3112;&#3149;&#3120;&#3134;&#3120;&#3137;','footer_tagline':'&#3128;&#3149;&#3039;&#3134;&#3120;&#3149;&#3103;&#3149; &#3078;&#3120; &#3112;&#3120;&#3149;&#3116;&#3119;&#3108;&#3147; &#3092;&#3134;&#3120;&#3108; &#3120;&#3136;&#3108;&#3137;&#3122;&#3137;&#3112;&#3137; &#3123;&#3056;&#3149;&#3108;&#3135;&#3125;&#3074;&#3108;&#3074; &#3127;&#3143;&#3119;&#3074;&#3078;&#3108;&#3074;'}
};
function applyLanguage(lang) {
    const dict = translations[lang];
    if (!dict) return;
    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (dict[key]) el.textContent = dict[key];
    });
    document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.classList.toggle('active', btn.dataset.lang === lang);
    });
}
function switchLang(lang) {
    localStorage.setItem('farmprice_lang', lang);
    applyLanguage(lang);
}
document.addEventListener('DOMContentLoaded', function() {
    const saved = localStorage.getItem('farmprice_lang') || 'en';
    applyLanguage(saved);
});
</script>
</body>
</html>"""

with open('crops/templates/crops/landing.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done!')