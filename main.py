import ltk

width = ltk.window.innerWidth
height = ltk.window.innerHeight

class Main(ltk.Widget):
    def __init__(self, *items):
        ltk.Widget.__init__(
            self,
            *items
        )
        self.width(1500).height(850).attr("id", "main")


class Item(ltk.Widget):
    count = 0
    classes = [ "item" ]
    def __init__(self, x, y, width, title, label, src, url):
        ltk.Widget.__init__(
            self,
            ltk.Link(
                url,
                ltk.VBox(
                    ltk.Text(title).css("text-align", "center")
                        .css("font-size", 20)
                        .css("margin-bottom", -2),
                    ltk.Image(src)
                        .css("border", "5px solid transparent")
                        .on("mouseenter", ltk.proxy(
                            lambda e: ltk.find(e.target).css("border-color", "orange")
                        ))
                        .on("mouseleave", ltk.proxy(
                            lambda e: ltk.find(e.target).css("border-color", "transparent")
                        )),
                    ltk.Text(label).css("text-align", "center")
                        .css("font-size", 20)
                ),
            )
            .attr("id", f"item-{Item.count}")
            .attr("target", "_blank")
            .css("position", "absolute")
            .css("text-decoration", "none")
            .css("left", (80 + x))
            .css("top", (40 + y))
            .css("width", width)
            .css("opacity", 0)
            .addClass("item")
        )
        Item.count += 1

items = [
    Item(
        0,
        0,
        300,
        "",
        "Chris Laffra",
        "https://chrislaffra.com/chris.png",
        "https://chrislaffra.com",
    ),
    Item(
        0,
        500,
        100,
        "1991",
        "OO Graphics",
        "https://chrislaffra.com/book-oo-graphics.png",
        "https://link.springer.com/book/10.1007/978-3-642-79192-5",
    ),
    Item(
        120,
        450,
        100,
        "1992",
        "Ph.D.",
        "https://chrislaffra.com/book-procol.png",
        "https://www.bibliotheek.nl/catalogus/titel.093231113.html/procol/",
    ),
    Item(
        240,
        350,
        100,
        "1996",
        "Java",
        "https://chrislaffra.com/book-java.png",
        "https://books.google.com/books/about/Advanced_Java.html?id=OoV0QgAACAAJ&redir_esc=y",
    ),
    Item(
        300,
        550,
        120,
        "1994-1997",
        "C++ & Java",
        "https://chrislaffra.com/ms.png",
        "https://sep.stanford.edu/oldsep/matt/jest/C2j/c2j.html",
    ),
    Item(
        360,
        250,
        100,
        "2004",
        "Eclipse FAQs",
        "https://chrislaffra.com/book-eclipse.png",
        "https://www.amazon.com/exec/obidos/ASIN/0321268385",
    ),
    Item(
        450,
        440,
        120,
        "2006-2010",
        "VisualAge MicroEdition",
        "https://chrislaffra.com/IBM.png",
        "https://cacm.acm.org/magazines/2003/8/6747-extracting-library-based-java-applications/abstract",
    ),
    Item(
        580,
        550,
        120,
        "2012",
        "Python",
        "https://chrislaffra.com/quartz.png",
        "https://www.quora.com/When-why-and-to-what-extent-did-Bank-of-America-rebuild-its-entire-tech-stack-with-Python",
    ),
    Item(
        580,
        170,
        180,
        "2015",
        "AppMaker",
        "https://chrislaffra.com/google.png",
        "https://en.wikipedia.org/wiki/Google_App_Maker",
    ),
    Item(
        680,
        10,
        180,
        "2016",
        "Teams",
        "https://chrislaffra.com/google.png",
        "https://cloud.google.com/developers/corp-eng",
    ),
    Item(
        720,
        300,
        180,
        "2016",
        "GVC",
        "https://chrislaffra.com/google.png",
        "https://workspace.google.com/blog/productivity-collaboration/how-google-went-all-video-meetings-and-you-can-too",
    ),
    Item(
        800,
        500,
        150,
        "2018",
        "Developer Productivity",
        "https://chrislaffra.com/uber.png",
        "https://twitter.com/laffra/status/1153639626252443649",
    ),
    Item(
        920,
        50,
        150,
        "2021",
        "C4E",
        "https://chrislaffra.com/book-c4e.png",
        "https://chrislaffra.com/c4e.html",
    ),
    Item(
        1090,
        130,
        90,
        "JPM 2022",
        "Athena - Python",
        "https://chrislaffra.com/JPM.png",
        "https://www.linkedin.com/posts/chrislaffra_i-am-happy-to-share-that-the-jp-morgan-python-activity-6944339599607382016-HWQU/?utm_source=linkedin_share&utm_medium=member_desktop_web",
    ),
    Item(
        1100,
        450,
        120,
        "2022",
        "Productivity",
        "https://chrislaffra.com/book-secret.png",
        "https://chrislaffra.com/c4e.html#book2",
    ),
    Item(
        1210,
        -60,
        240,
        "2024",
        "C4E",
        "https://chrislaffra.com/book-xebia.png",
        "https://xebia.com/academy/nl/training/communication-for-engineers/",
    ),
    Item(
        1320,
        380,
        120,
        "2024",
        "PySheets",
        "https://chrislaffra.com/pysheets.png",
        "https://github.com/laffra/excel-in-python",
    ),
    Item(
        1350,
        580,
        70,
        "2024",
        "LTK",
        "https://chrislaffra.com/ltk.png",
        "https://laffra.github.io/ltk/",
    ),
]

def tile(url, image, label, width=120, height=120):
    return ltk.Link(url,
        ltk.VBox(
            ltk.Image(f"https://chrislaffra.com/{image}")
                .css("border", "5px solid transparent")
                .on("mouseenter", ltk.proxy(
                    lambda e: ltk.find(e.target).css("border-color", "orange")
                ))
                .on("mouseleave", ltk.proxy(
                    lambda e: ltk.find(e.target).css("border-color", "transparent")
                ))
                .css("width", width)
                .css("height", height),
            ltk.Text(label).css("font-size", 20)
        )
        .css("float", "left")
        .css("width", 120)
        .css("margin", 25)
        .css("align-items", "center")
        .css("text-align", "center")
    ).attr("target", "_blank")

tiles = [
    tile("https://laffra.github.io/ltk/", "ltk.png", "LTK"),
    tile("https://micrologai.github.io/microlog/#examples-dataframes/2023_07_31_11_15_57/", "microlog.png", "Microlog"),
    tile("https://github.com/laffra/excel-in-python", "pysheets.png", "PySheets"),
    tile("https://xebia.com/academy/nl/training/communication-for-engineers/", "xebia.jpeg", "Xebia"),
    tile("https://chrislaffra.com/c4e", "c4e-black.jpg", "C4E", 76),
    tile("https://www.youtube.com/watch?v=GpXZPEMFPtU&list=PLXHJZN4UnprtCWGih6gSG_PvmgsvHue5y&index=3", "beyondcoding.png", "10X"),
    tile("https://techleadjournal.dev/episodes/48", "tlj.png", "TLJ"),
    tile("https://www.youtube.com/playlist?list=PLXHJZN4UnprtCWGih6gSG_PvmgsvHue5y", "YouTube.png", "Youtube "),
    tile("https://techhub.social/@laffra", "icon-mastodon.webp", "Mastodon"),
    tile("http://www.linkedin.com/in/chrislaffra", "icon-linkedin.jpeg", "LinkedIn "),
    tile("http://github.com/laffra", "icon-github.png", "Github"),
    tile("https://medium.com/@laffra", "medium-logo.png", "Medium"),
    tile("https://chrislaffra.com/chris_laffra_resume.pdf", "resume.png", "Resume "),
    tile("https://github.com/laffra/cacophonia", "cacophonia.png", "Cacophonia"),
    tile("https://github.com/laffra/happymac", "happymac.png", "HappyMac"),
    tile("https://www.linkedin.com/pulse/how-prepare-technical-interview-google-amazon-linkedin-chris-laffra/", "icon-whiteboard.png", "Interviewing"),
    tile("https://chrislaffra.com/whackamole", "cross_128.png", "WhackAMole"),
    tile("http://chrislaffra.blogspot.com/", "icon-blogger.png", "Blog "),
    tile("http://www.curry-on.org/2019/", "curryon2019.png", "CurryOn"),
    tile("http://pyalgoviz.appspot.com/", "pyalgoviz.ico", " PyAlgoViz "),
    tile("http://pyalgoviz.appspot.com/oscon", "oscon.png", " OSCON "),
    tile("http://pyalgoviz.appspot.com/demo", "pydata.jpeg", " PyData&nbsp;SV "),
    tile("https://us.pycon.org/2014/schedule/presentation/96/", "pycon2014.png", "Pycon"),
    tile("https://twitter.com/laffra", "icon-twitter.jpeg", "Twitter "),
    tile("http://www.amazon.com/Official-Eclipse-FAQs-John-Arthorne/dp/0321268385", "icon-eclipse-faq.jpg", "Eclipse "),
    tile("http://www.slideshare.net/chrislaffra", "icon-slideshare.jpeg", "Slides "),
    tile("https://www.google.com/search?tbo=p&amp;tbm=pts&amp;hl=en&amp;q=ininventor:laffra", "icon-patent.png", "Patents "),
    tile("http://www.informatik.uni-trier.de/~ley/pers/hd/l/Laffra:Chris.html#!", "icon-journals.png", "Journals "),
    tile("https://www.facebook.com/public/Chris-Laffra", "icon-facebook.jpeg", "Facebook "),
]

(
    ltk.VBox(
        ltk.Heading1("Chris Laffra").css("font-size", 32).css("text-align", "center"),
        Main(*items).css("position", "relative")
            .css("margin-bottom", 50),
        ltk.VBox(
            ltk.Heading2("For more details select any item shown in the visual resume above or in the list below")
                .css("color", "gray")
                .css("text-align", "center"),
            ltk.Div(*tiles)
                .attr("id", "tiles")
        )
        .css("width", width - 50)
        .css("margin-left", width * 0.1)
        .css("align-items", "center")
        .css("margin", "auto")
        .attr("id", "rest")
        .css("opacity", 0)
    )
    .css("width", "100%")
    .css("margin", "auto")
    .appendTo(ltk.window.document.body)
)

items = ltk.find_list(".item .ltk-a")

def get_line(n):
    start = items[n]
    end = items[n+1]
    x1 = ltk.parse_float(start.css("left")) + start.width() / 2
    y1 = ltk.parse_float(start.css("top")) + start.height() / 2
    x2 = ltk.parse_float(end.css("left")) + end.width() / 2
    y2 = ltk.parse_float(end.css("top")) + end.height() / 2
    return f'<line id="line-{n}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" style="stroke:white;stroke-dasharray:5,5;stroke-width:2" />'

ltk.find("#main").append(
    ltk.create(f"""
        <svg id="svg" height="850" width="1500">
            <line x1="40" y1="20" x2="40" y2="800" style="stroke:lightgray;stroke-width:2" />
            <line x1="0" y1="770" x2="1500" y2="770" style="stroke:lightgray;stroke-width:2" />

            <text x="200" y="807" style="font-size:16pt; fill:gray">noob</text>
            <text x="1300" y="807" style="font-size:16pt; fill:gray">now</text>
            <text x="730" y="807" style="font-size:16pt; fill:lightgray">time</text>

            <line x1="600" y1="800" x2="700" y2="800" style="stroke:lightgray;stroke-width:2" />
            <line x1="900" y1="800" x2="880" y2="790" style="stroke:lightgray;stroke-width:2" />
            <line x1="900" y1="800" x2="880" y2="810" style="stroke:lightgray;stroke-width:2" />

            <line x1="800" y1="800" x2="900" y2="800" style="stroke:lightgray;stroke-width:2" />
            <line x1="600" y1="800" x2="620" y2="790" style="stroke:lightgray;stroke-width:2" />
            <line x1="600" y1="800" x2="620" y2="810" style="stroke:lightgray;stroke-width:2" />

            <text style="font-size:16pt; fill:gray;" transform="translate(28,85) rotate(270)">Human</text>
            <text style="font-size:16pt; fill:gray;" transform="translate(28,685) rotate(270)">Technical</text>
            <text style="font-size:16pt; fill:lightgray;" transform="translate(28,385) rotate(270)">focus</text>

            <line x1="20" y1="200" x2="20" y2="300" style="stroke:lightgray;stroke-width:2" />
            <line x1="10" y1="220" x2="20" y2="200" style="stroke:lightgray;stroke-width:2" />
            <line x1="30" y1="220" x2="20" y2="200" style="stroke:lightgray;stroke-width:2" />

            <line x1="20" y1="420" x2="20" y2="520" style="stroke:lightgray;stroke-width:2" />
            <line x1="10" y1="500" x2="20" y2="520" style="stroke:lightgray;stroke-width:2" />
            <line x1="30" y1="500" x2="20" y2="520" style="stroke:lightgray;stroke-width:2" />

            { "".join([get_line(n) for n in range(1, len(items) - 1)]) }
        </svg>
    """).css("margin", "auto")
)

def show(index):
    ltk.find(f"#line-{index - 1}").css("stroke", "pink")
    item = ltk.find(f"#item-{index}")
    body = ltk.find("html, body")
    if not item.length:
        ltk.find("#rest").animate(ltk.to_js({ "opacity": 1 }), 1000)
        body.animate(ltk.to_js({ "scrollTop": height - 800 }), 1500, 'swing', lambda:
            body.animate(ltk.to_js({ "scrollTop": 0 }), 300, 'swing')
        )
        # ltk.find("#main").animate(ltk.to_js({ "left": 0 }))
        return
    x = ltk.parse_float(item.css("left"))
    y = ltk.parse_float(item.css("top"))
    w = item.width()
    h = item.height()
    item.css(ltk.to_js({
        "left": x + w / 2,
        "top": y + h / 2,
        "width": 0,
        "height": 0,
    })).animate(
        ltk.to_js({
            "top": y,
            "left": x,
            "width": w,
            "height": h,
            "opacity": 1,
        }),
        600 - (17 - index) * 30, 
        lambda: show(index + 1)
    )
    if x > width - 200:
        ltk.find("#main").animate(
            ltk.to_js({
                "left": -x + width * 3 /4,
            }), 200
        )

show(0)
