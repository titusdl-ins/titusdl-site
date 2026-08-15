import base64, pathlib

base = pathlib.Path(__file__).parent
tpl = (base / "template.html").read_text()

samples = [
    dict(
        file="sample-1-responsive.html",
        img="images/photo6-genuine-help.jpg",
        position="center 30%",
        title="Sample 1 — Never Miss a Follow-Up",
        label="Sample 1 / 5 — Responsiveness",
        eyebrow="Built for how fast clients expect an answer",
        headline="The client who calls today shouldn&rsquo;t wait until tomorrow.",
        subhead="Slow response is the number one reason agents lose renewals to a competitor. Every client, every open item, one screen &mdash; so nothing waits on your memory.",
        pain="A renewal slips through the cracks and the client leaves for someone else.",
        solution="Renewal, RMD &amp; Medicare-65 dates calculate themselves &mdash; nothing depends on remembering.",
    ),
    dict(
        file="sample-2-family.html",
        img="images/photo7-family-real.jpg",
        position="center 22%",
        title="Sample 2 — One Family, One Record",
        label="Sample 2 / 5 — Family & Household",
        eyebrow="Built for the whole household, not just one policy",
        headline="Three generations. One family. One record that stays connected.",
        subhead="When a family&rsquo;s policies live in five disconnected records, you miss the cross-sell and the client feels like a stranger every time they call.",
        pain="A family&rsquo;s policies live in five different, disconnected records.",
        solution="Family &amp; joint policies linked automatically &mdash; one household, one view.",
    ),
    dict(
        file="sample-3-medicare.html",
        img="images/photo3-medicare.jpg",
        position="center 35%",
        title="Sample 3 — Medicare-65, Handled",
        label="Sample 3 / 5 — Senior & Medicare Clients",
        eyebrow="Built for the clients who need the most patience",
        headline="When Medicare-65 hits, you&rsquo;ll already know &mdash; before they call asking.",
        subhead="Senior clients don&rsquo;t want to be sold to twice. Renewal and Medicare-65 eligibility dates calculate themselves the moment you open a record, so you reach out first.",
        pain="A renewal or eligibility date gets missed, and a longtime client feels forgotten.",
        solution="Medicare-65, renewal, and RMD dates calculated automatically &mdash; you reach out first.",
    ),
    dict(
        file="sample-4-organized.html",
        img="images/photo10-excel.jpg",
        position="center 30%",
        title="Sample 4 — From Chaos to Control",
        label="Sample 4 / 5 — Organization",
        eyebrow="Built for the end of the day you can&rsquo;t keep working",
        headline="No single spreadsheet has the whole client &mdash; so you keep switching between six.",
        subhead="Client info scattered across spreadsheet tabs, old emails, and sticky notes means bouncing between them for one answer. One searchable client book ends that.",
        pain="Client info scattered across spreadsheet tabs, old emails, and sticky notes.",
        solution="One searchable client book &mdash; every policy, every family, in one place.",
    ),
    dict(
        file="sample-5-onthego.html",
        img="images/photo1-trust.jpg",
        position="center 30%",
        title="Sample 5 — Everything, On the Go",
        label="Sample 5 / 5 — Mobile & In-Field",
        eyebrow="Built for the meeting that isn&rsquo;t at your desk",
        headline="Everything you know about this client &mdash; in your hand, right now.",
        subhead="Your best conversations happen outside the office. The same client record is right there on your phone or tablet, mid-meeting.",
        pain="You&rsquo;re one step behind because the client file is back at your desk.",
        solution="A responsive web app &mdash; the same client book on phone, tablet, or desktop.",
    ),
]

for s in samples:
    img_path = base / s["img"]
    data = base64.b64encode(img_path.read_bytes()).decode("ascii")
    data_uri = f"data:image/jpeg;base64,{data}"

    out = tpl
    out = out.replace("__TITLE__", s["title"])
    out = out.replace("__IMAGE__", data_uri)
    out = out.replace("__POSITION__", s["position"])
    out = out.replace("__SAMPLE_LABEL__", s["label"])
    out = out.replace("__EYEBROW__", s["eyebrow"])
    out = out.replace("__HEADLINE__", s["headline"])
    out = out.replace("__SUBHEAD__", s["subhead"])
    out = out.replace("__PAIN__", s["pain"])
    out = out.replace("__SOLUTION__", s["solution"])

    out_path = base / s["file"]
    out_path.write_text(out)
    print(s["file"], len(out) // 1024, "KB")
