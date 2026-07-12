import os

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Developer Profile</title>
  <style>
    :root {
      --bg: #0d1117;
      --surface: #161b22;
      --text: #c9d1d9;
      --accent: #58a6ff;
      --muted: #8b949e;
      font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
    }

    * {
      box-sizing: border-box;
    }

    body {
      margin: 0;
      padding: 0;
      background: radial-gradient(circle at top, #161b22 0%, #0d1117 35%, #0b1220 100%);
      color: var(--text);
    }

    .page {
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 2rem;
    }

    .card {
      width: min(1000px, 100%);
      background: rgba(15, 23, 42, 0.95);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 24px;
      padding: 2.5rem;
      box-shadow: 0 24px 80px rgba(0, 0, 0, 0.45);
      backdrop-filter: blur(14px);
    }

    .header {
      display: grid;
      grid-template-columns: auto 1fr;
      gap: 1.75rem;
      align-items: center;
      margin-bottom: 2rem;
    }

    .avatar {
      width: 140px;
      height: 140px;
      border-radius: 28px;
      background: linear-gradient(135deg, #58a6ff 0%, #79c0ff 100%);
      display: grid;
      place-items: center;
      color: #0b1220;
      font-size: 3rem;
      font-weight: 700;
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
    }

    .header-info h1 {
      margin: 0;
      font-size: 2.75rem;
      letter-spacing: -0.03em;
    }

    .header-info p {
      margin: 0.5rem 0 0;
      color: var(--muted);
      max-width: 680px;
      line-height: 1.75;
    }

    .section-title {
      display: inline-flex;
      align-items: center;
      gap: 0.75rem;
      margin-bottom: 1rem;
      font-size: 0.95rem;
      text-transform: uppercase;
      letter-spacing: 0.2em;
      color: var(--accent);
    }

    .grid {
      display: grid;
      gap: 1.5rem;
    }

    .grid-2 {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .panel {
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.06);
      border-radius: 20px;
      padding: 1.5rem;
    }

    .panel h2 {
      margin: 0 0 1rem;
      font-size: 1.25rem;
      color: #f0f6fc;
    }

    .panel p,
    .panel li,
    .panel a {
      color: var(--text);
    }

    .panel ul {
      margin: 0;
      padding-left: 1.25rem;
      line-height: 1.7;
    }

    .panel li {
      margin-bottom: 0.75rem;
    }

    .tag-list {
      display: flex;
      flex-wrap: wrap;
      gap: 0.75rem;
      margin: 0;
      padding: 0;
      list-style: none;
    }

    .tag-list li {
      padding: 0.65rem 1rem;
      border-radius: 999px;
      background: rgba(88, 166, 255, 0.12);
      color: #8b949e;
      font-size: 0.95rem;
    }

    .footer {
      margin-top: 1.5rem;
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;
      color: var(--muted);
      font-size: 0.95rem;
    }

    .footer a {
      color: var(--accent);
      text-decoration: none;
    }

    @media (max-width: 720px) {
      .header {
        grid-template-columns: 1fr;
        text-align: center;
      }

      .header-info h1 {
        font-size: 2.25rem;
      }

      .grid-2 {
        grid-template-columns: 1fr;
      }
    }
  </style>
</head>
<body>
  <main class="page">
    <section class="card">
      <div class="header">
        <div class="avatar">GH</div>
        <div class="header-info">
          <h1>Developer Profile</h1>
          <p>
            Transform your GitHub profile into a polished developer landing page. Showcase projects, skills,
            and contact details in a clean, code-focused presentation.
          </p>
        </div>
      </div>

      <div class="grid grid-2">
        <div class="panel">
          <div class="section-title">About</div>
          <p>
            A modern developer page layout designed to feel like a GitHub profile but optimized for technical
            presentation. Use this page as a template for your personal site, portfolio, or README-style profile.
          </p>
          <ul class="tag-list">
            <li>Python</li>
            <li>HTML</li>
            <li>CSS</li>
            <li>Web UI</li>
            <li>Portfolio</li>
          </ul>
        </div>

        <div class="panel">
          <div class="section-title">Featured Projects</div>
          <ul>
            <li><strong>Profile Reimagined</strong> — Custom developer landing page design.</li>
            <li><strong>Repo Explorer</strong> — Showcase GitHub repos with summary cards.</li>
            <li><strong>API Dashboard</strong> — Build an interactive project status board.</li>
          </ul>
        </div>
      </div>

      <div class="grid" style="margin-top: 1.75rem;">
        <div class="panel">
          <h2>Skills</h2>
          <ul class="tag-list">
            <li>Frontend</li>
            <li>Backend</li>
            <li>DevOps</li>
            <li>UX/UI</li>
            <li>Automation</li>
          </ul>
        </div>

        <div class="panel">
          <h2>Contact</h2>
          <p>Share your GitHub username, email, and social links to connect with collaborators.</p>
          <ul>
            <li>GitHub: github.com/your-username</li>
            <li>Portfolio: yoursite.dev</li>
            <li>Email: you@example.com</li>
          </ul>
        </div>
      </div>

      <div class="footer">
        <span>Built with Python-generated HTML and embedded CSS.</span>
        <a href="#">Open in browser</a>
      </div>
    </section>
  </main>
</body>
</html>
"""

output_file = os.path.join(os.path.dirname(__file__), "github_developer_profile.html")

with open(output_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Developer profile page generated: {output_file}")
