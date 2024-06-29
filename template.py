documentTemplate = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Legal Document</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        .container {
            margin: 20px;
            padding: 20px;
            border: 1px solid #000;
        }
        header {
            text-align: center;
            margin-bottom: 40px;
        }
        h1 {
            font-size: 24px;
            margin-bottom: 10px;
        }
        h2 {
            font-size: 20px;
            margin-bottom: 10px;
        }
        h3 {
            font-size: 18px;
            margin-bottom: 10px;
        }
        p {
            margin-bottom: 15px;
        }
        .clause {
            margin-bottom: 30px;
        }
        .signature-section {
            display: flex;
            justify-content: space-between;
            margin-top: 50px;
        }
        .signature {
            width: 40%;
            text-align: center;
        }
        .signature div {
            margin-bottom: 40px;
        }
        .signature-line {
            display: inline-block;
            width: 200px;
            border-bottom: 1px solid #000;
            margin-top: 30px;
        }
        .signature-title {
            margin-top: 5px;
            font-size: 14px;
        }
        .page-break {
            page-break-before: always;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Legal Agreement</h1>
            <p>Effective Date: [Insert Date]</p>
        </header>

        <section class="clause">
            <h2>1. Introduction</h2>
            <p>This Legal Agreement (the "Agreement") is made and entered into as of the effective date set forth above by and between [Party A] ("Party A") and [Party B] ("Party B").</p>
        </section>

        <section class="clause">
            <h2>2. Definitions</h2>
            <p>For purposes of this Agreement, the following terms shall have the meanings set forth below:</p>
            <h3>2.1. Confidential Information</h3>
            <p>"Confidential Information" means any information disclosed by either party to the other, either directly or indirectly, in writing, orally, or by inspection of tangible objects...</p>
            <h3>2.2. Services</h3>
            <p>"Services" means the services to be provided by [Party A/Party B] as described in [Exhibit A/Attachment 1].</p>
        </section>

        <section class="clause">
            <h2>3. Obligations of the Parties</h2>
            <p>Each party agrees to perform its obligations as set forth in this Agreement.</p>
            <h3>3.1. Party A Obligations</h3>
            <p>Party A shall provide the following services...</p>
            <h3>3.2. Party B Obligations</h3>
            <p>Party B shall compensate Party A as described in [Exhibit B/Attachment 2]...</p>
        </section>

        <section class="clause">
            <h2>4. Term and Termination</h2>
            <p>This Agreement shall commence on the Effective Date and continue until terminated by either party upon [number] days' written notice.</p>
        </section>

        <section class="clause">
            <h2>5. Miscellaneous</h2>
            <h3>5.1. Governing Law</h3>
            <p>This Agreement shall be governed by and construed in accordance with the laws of [State/Country].</p>
            <h3>5.2. Entire Agreement</h3>
            <p>This Agreement constitutes the entire agreement between the parties and supersedes all prior agreements and understandings, whether written or oral, relating to the subject matter hereof.</p>
        </section>

        <div class="signature-section">
            <div class="signature">
                <p>________________________</p>
                <p class="signature-line"></p>
                <p class="signature-title">Party A Signature</p>
            </div>
            <div class="signature">
                <p>________________________</p>
                <p class="signature-line"></p>
                <p class="signature-title">Party B Signature</p>
            </div>
        </div>

        <div class="page-break"></div>

        <section class="clause">
            <h2>Exhibit A</h2>
            <p>Description of Services</p>
        </section>

        <section class="clause">
            <h2>Exhibit B</h2>
            <p>Compensation Details</p>
        </section>
    </div>
</body>
</html>
"""

documentTemplate1 = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Legal Document</title>
    <style>
        body {
            font-family: 'Times New Roman', Times, serif;
            font-size: 14pt;
            line-height: 1.6;
            margin: 40px;
            padding: 0;
        }
        header {
            text-align: center;
            margin-bottom: 40px;
        }
        h1 {
            font-size: 26pt;
            margin-bottom: 10px;
        }
        h2 {
            font-size: 22pt;
            margin-bottom: 10px;
        }
        h3 {
            font-size: 20pt;
            margin-bottom: 10px;
        }
        p {
            margin-bottom: 15px;
        }
        .clause {
            margin-bottom: 30px;
        }
        .signature-section {
            display: flex;
            justify-content: space-between;
            margin-top: 50px;
        }
        .signature {
            width: 40%;
            text-align: center;
        }
        .signature div {
            margin-bottom: 40px;
        }
        .signature-line {
            display: inline-block;
            width: 200px;
            border-bottom: 1px solid #000;
            margin-top: 30px;
        }
        .signature-title {
            margin-top: 5px;
            font-size: 14pt;
        }
        .page-break {
            page-break-before: always;
        }
    </style>
</head>
<body>
    <header>
        <h1>Legal Agreement</h1>
        <p>Effective Date: [Insert Date]</p>
    </header>

    <section class="clause">
        <h2>1. Introduction</h2>
        <p>This Legal Agreement (the "Agreement") is made and entered into as of the effective date set forth above by and between [Party A] ("Party A") and [Party B] ("Party B").</p>
    </section>

    <section class="clause">
        <h2>2. Definitions</h2>
        <p>For purposes of this Agreement, the following terms shall have the meanings set forth below:</p>
        <h3>2.1. Confidential Information</h3>
        <p>"Confidential Information" means any information disclosed by either party to the other, either directly or indirectly, in writing, orally, or by inspection of tangible objects...</p>
        <h3>2.2. Services</h3>
        <p>"Services" means the services to be provided by [Party A/Party B] as described in [Exhibit A/Attachment 1].</p>
    </section>

    <section class="clause">
        <h2>3. Obligations of the Parties</h2>
        <p>Each party agrees to perform its obligations as set forth in this Agreement.</p>
        <h3>3.1. Party A Obligations</h3>
        <p>Party A shall provide the following services...</p>
        <h3>3.2. Party B Obligations</h3>
        <p>Party B shall compensate Party A as described in [Exhibit B/Attachment 2]...</p>
    </section>

    <section class="clause">
        <h2>4. Term and Termination</h2>
        <p>This Agreement shall commence on the Effective Date and continue until terminated by either party upon [number] days' written notice.</p>
    </section>

    <section class="clause">
        <h2>5. Miscellaneous</h2>
        <h3>5.1. Governing Law</h3>
        <p>This Agreement shall be governed by and construed in accordance with the laws of [State/Country].</p>
        <h3>5.2. Entire Agreement</h3>
        <p>This Agreement constitutes the entire agreement between the parties and supersedes all prior agreements and understandings, whether written or oral, relating to the subject matter hereof.</p>
    </section>

    <div class="signature-section">
        <div class="signature">
            <p>________________________</p>
            <p class="signature-line"></p>
            <p class="signature-title">Party A Signature</p>
        </div>
        <div class="signature">
            <p>________________________</p>
            <p class="signature-line"></p>
            <p class="signature-title">Party B Signature</p>
        </div>
    </div>

    <div class="page-break"></div>

    <section class="clause">
        <h2>Exhibit A</h2>
        <p>Description of Services</p>
    </section>

    <section class="clause">
        <h2>Exhibit B</h2>
        <p>Compensation Details</p>
    </section>
</body>
</html>
"""