from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors

# Define slide titles and content
slides_content = [
    ("Impact of Globalization on International Business",
     "Opportunities and Challenges in a Global Economy\nYour Name-Molly Kumari | Date-20/03/25 | Institution- Sri venketeswara college"),
    ("Introduction",
     "• Globalization: Integration of markets, economies, and cultures globally.\n• Importance: Drives trade, investment, and technology exchange."),
    ("Positive Impacts",
     "1. Market Expansion – Access to new customers worldwide.\n2. Access to Resources – Cheaper labor, materials, and technology.\n3. Foreign Investment – Boosts economies and creates jobs.\n4. Innovation & Technology Transfer – Faster spread of innovations globally."),
    ("More Positive Impacts",
     "5. Diverse Talent Pool – Global hiring improves skills and perspectives.\n6. Competitive Advantage – Encourages efficiency and quality."),
    ("Negative Impacts",
     "1. Intense Competition – Local businesses may suffer.\n2. Cultural Barriers – Language and customs can hinder success.\n3. Economic Dependency – Vulnerable to global shocks (e.g., pandemics, wars)."),
    ("More Negative Impacts",
     "4. Environmental Issues – Pollution, resource depletion, climate impact.\n5. Labor Exploitation – Poor working conditions in developing nations.\n6. Loss of Local Identity – Global brands overshadow local businesses."),
    ("Case Studies (Optional)",
     "• Example 1: Apple’s global supply chain\n• Example 2: Impact on local industries (e.g., textiles in developing countries)"),
    ("Conclusion",
     "• Globalization offers growth but also brings challenges.\n• Success requires adaptability, cultural sensitivity, and sustainability.\n• Future: Balance global integration and local identity.")
]

# Create a PDF file with attractive PPT-style design
pdf_path = "/mnt/data/Impact_of_Globalization_on_International_Business.pdf"
c = canvas.Canvas(pdf_path, pagesize=letter)
width, height = letter

def draw_slide(title, content, canvas_obj):
    header_height = 1 * inch
    footer_height = 0.5 * inch
    
    # Draw background (simulate a subtle gradient with a solid color)
    canvas_obj.setFillColor(colors.lightblue)
    canvas_obj.rect(0, 0, width, height, fill=True, stroke=False)

    # Draw header (dark blue) at the top
    canvas_obj.setFillColor(colors.darkblue)
    canvas_obj.rect(0, height - header_height, width, header_height, fill=True, stroke=False)

    # Draw footer (dark blue) at the bottom
    canvas_obj.rect(0, 0, width, footer_height, fill=True, stroke=False)

    # Draw slide title in header (white text)
    canvas_obj.setFillColor(colors.white)
    canvas_obj.setFont("Helvetica-Bold", 20)
    canvas_obj.drawCentredString(width / 2, height - 0.65 * inch, title)

    # Draw content text in the middle area
    canvas_obj.setFillColor(colors.black)
    canvas_obj.setFont("Helvetica", 14)
    text_object = canvas_obj.beginText()
    text_object.setTextOrigin(inch, height - header_height - 0.75 * inch)
    text_object.setLeading(20)
    for line in content.split("\n"):
        text_object.textLine(line)
    canvas_obj.drawText(text_object)

# Loop through each slide and add it to the PDF with slide numbers in the footer
for idx, (title, content) in enumerate(slides_content, start=1):
    draw_slide(title, content, c)

    # Add slide number in the footer (white text)
    c.setFillColor(colors.white)
    c.setFont("Helvetica", 12)
    slide_number_text = f"Slide {idx} of {len(slides_content)}"
    c.drawCentredString(width / 2, 0.2 * inch, slide_number_text)

    c.showPage()

# Save the PDF file
c.save()

pdf_path









