# ⚡ Electric Lightning Background - Testing Guide

## ✅ Installation Complete!

Your electric lightning background has been successfully applied to **all 15 pages** of your SDG 7 Dashboard!

## 🎯 What Was Done

### 1. Created CSS File
- **Location**: `sustainable_energy/static/css/electric-background.css`
- **Effect**: Animated electric blue lightning with pulsing glow
- **Colors**: Deep navy (#001a33) to electric cyan (#6dd5ed)

### 2. Updated All Templates
All 15 HTML templates now include:
```html
{% load static %}
<link rel="stylesheet" href="{% static 'css/electric-background.css' %}">
<body class="electric-bg">
```

### 3. Pages Updated
✅ Main Dashboard (index.html)
✅ Objective Selector
✅ Objectives 1-8
✅ Email Alert Pages (3 pages)
✅ Email Logs
✅ Admin Login

## 🚀 How to Test

### Step 1: Restart Django Server
```bash
cd sustainable_energy
python manage.py runserver
```

### Step 2: Clear Browser Cache
- **Chrome/Edge**: Press `Ctrl + Shift + Delete` → Clear cached images and files
- **Quick method**: Press `Ctrl + F5` for hard refresh

### Step 3: Visit Any Page
Open your browser and go to:
- http://127.0.0.1:8000/
- http://127.0.0.1:8000/objective-selector/
- http://127.0.0.1:8000/objective3/
- Any other page!

## 🎨 What You Should See

### Background Effect:
- **Deep blue base** - Dark navy background
- **Electric glow** - Bright cyan/blue glow in the center
- **Pulsing animation** - Smooth 4-second pulse cycle
- **Professional look** - Matches your energy theme perfectly

### Content:
- White cards remain clearly visible
- Text is easy to read
- All functionality works normally
- Background doesn't interfere with interactions

## 🔧 Customization (Optional)

### Make it Brighter:
Edit `sustainable_energy/static/css/electric-background.css`:
```css
@keyframes electricPulse {
    0%, 100% {
        opacity: 0.9;  /* Increase from 0.7 */
    }
    50% {
        opacity: 1;
    }
}
```

### Make it Pulse Faster:
```css
animation: electricPulse 2s ease-in-out infinite;
                        /* ^ Change from 4s to 2s */
```

### Change the Color:
```css
rgba(109, 213, 237, 0.6)  /* Electric blue */
/* Try: */
rgba(0, 255, 255, 0.6)    /* Brighter cyan */
rgba(100, 200, 255, 0.6)  /* Lighter blue */
```

## 📸 Optional: Use Your Actual Image

If you want to use your exact lightning image instead of the CSS effect:

### Step 1: Save the Image
Save your electric lightning image as:
```
sustainable_energy/static/images/electric-lightning.jpg
```

### Step 2: Update CSS
Add this to the top of `electric-background.css`:
```css
body.electric-bg {
    background-image: url('../images/electric-lightning.jpg') !important;
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}
```

## 🐛 Troubleshooting

### Background Not Showing?
1. **Check static files**:
   ```bash
   python manage.py collectstatic
   ```

2. **Verify settings.py**:
   ```python
   STATIC_URL = '/static/'
   STATICFILES_DIRS = [BASE_DIR / 'static']
   ```

3. **Hard refresh**: `Ctrl + F5`

### Background Too Dark/Bright?
Adjust the opacity values in the CSS file (see Customization section above)

### Animation Not Smooth?
- Check browser compatibility (works on Chrome, Firefox, Edge, Safari)
- Try reducing animation duration

## ✨ Result

Your dashboard now has a stunning, professional electric lightning background that:
- ✅ Matches the sustainable energy theme
- ✅ Looks modern and dynamic
- ✅ Works on all pages consistently
- ✅ Doesn't affect functionality
- ✅ Is fully customizable

## 📝 Files Created

1. `sustainable_energy/static/css/electric-background.css` - Main CSS file
2. `ELECTRIC_BACKGROUND_SETUP.md` - Setup documentation
3. `TEST_ELECTRIC_BACKGROUND.md` - This testing guide
4. `apply_electric_background.py` - Automation script
5. `fix_background_links.py` - Fix script

## 🎉 You're Done!

Just restart your server and refresh your browser. The electric lightning background is now live on all pages!

---

**Need help?** Check the CSS file for comments and customization options.
**Want to revert?** Simply remove the `<link>` tag from the templates.
