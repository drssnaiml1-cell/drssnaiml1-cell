"""Writes navy-and-gold GitHub stats and top-language cards for the profile page (run by the workflow)."""
import json
import os
import sys
import urllib.request

USER = os.environ.get("GH_USER", "drssnaiml1-cell")
TOKEN = os.environ["GITHUB_TOKEN"]
OUT = sys.argv[1] if len(sys.argv) > 1 else "dist"

Q = """query($login: String!) { user(login: $login) {
  followers { totalCount }
  contributionsCollection { totalCommitContributions restrictedContributionsCount totalPullRequestContributions
    totalIssueContributions contributionCalendar { totalContributions } }
  repositories(first: 100, ownerAffiliations: OWNER, isFork: false, privacy: PUBLIC) { totalCount nodes {
    stargazerCount forkCount languages(first: 10, orderBy: {field: SIZE, direction: DESC}) { edges { size node { name color } } } } } } }"""


def gql():
    req = urllib.request.Request("https://api.github.com/graphql", json.dumps({"query": Q, "variables": {"login": USER}}).encode(),
                                 {"Authorization": f"bearer {TOKEN}", "Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(req))["data"]["user"]


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;")


STYLE = """<style>.h{font:700 18px 'Segoe UI',Helvetica,Arial,sans-serif;fill:#C9A227}.l{font:400 14px 'Segoe UI',Helvetica,Arial,sans-serif;fill:#E8ECF4}
.v{font:700 14px 'Segoe UI',Helvetica,Arial,sans-serif;fill:#FFFFFF}.r{animation:in .6s ease-out backwards}
@keyframes in{from{opacity:0;transform:translateX(-8px)}to{opacity:1;transform:none}}</style>"""


def card(w, h, title, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{esc(title)}">'
            f'{STYLE}<rect width="{w}" height="{h}" rx="14" fill="#0B1F3A"/><rect width="{w}" height="3" fill="#C9A227"/>'
            f'<text x="24" y="38" class="h">{esc(title)}</text>{body}</svg>')


def main():
    u = gql()
    c = u["contributionsCollection"]
    repos = u["repositories"]["nodes"]
    rows = [("Contributions (last year)", c["contributionCalendar"]["totalContributions"]),
            ("Commits (incl. private)", c["totalCommitContributions"] + c["restrictedContributionsCount"]),
            ("Pull requests", c["totalPullRequestContributions"]), ("Public repositories", u["repositories"]["totalCount"]),
            ("Stars earned", sum(r["stargazerCount"] for r in repos)), ("Followers", u["followers"]["totalCount"])]
    body = "".join(f'<g class="r" style="animation-delay:{i * .1:.1f}s"><circle cx="30" cy="{68 + i * 26}" r="4" fill="#C9A227"/>'
                   f'<text x="44" y="{73 + i * 26}" class="l">{esc(k)}</text><text x="376" y="{73 + i * 26}" class="v" '
                   f'text-anchor="end">{v:,}</text></g>' for i, (k, v) in enumerate(rows))
    os.makedirs(OUT, exist_ok=True)
    open(f"{OUT}/stats.svg", "w").write(card(400, 230, "GitHub stats", body))
    langs = {}
    for r in repos:
        for e in r["languages"]["edges"]:
            n = e["node"]["name"]
            langs.setdefault(n, [0, e["node"]["color"] or "#C9A227"])[0] += e["size"]
    top = sorted(langs.items(), key=lambda kv: -kv[1][0])[:6]
    tot = sum(v[0] for _, v in top) or 1
    x, bar = 24, ""
    for n, (s, col) in top:
        w = 352 * s / tot
        bar += f'<rect x="{x:.1f}" y="56" width="{w:.1f}" height="10" fill="{col}"/>'
        x += w
    body = f'<clipPath id="c"><rect x="24" y="56" width="352" height="10" rx="5"/></clipPath><g clip-path="url(#c)">{bar}</g>'
    for i, (n, (s, col)) in enumerate(top):
        cx, cy = 30 + (i % 2) * 180, 98 + (i // 2) * 30
        body += (f'<g class="r" style="animation-delay:{i * .1:.1f}s"><circle cx="{cx}" cy="{cy - 5}" r="5" fill="{col}"/>'
                 f'<text x="{cx + 12}" y="{cy}" class="l">{esc(n)} <tspan class="v">{100 * s / tot:.1f}%</tspan></text></g>')
    open(f"{OUT}/languages.svg", "w").write(card(400, 230, "Top languages", body))
    print("stats written", rows, [n for n, _ in top])


if __name__ == "__main__":
    main()
