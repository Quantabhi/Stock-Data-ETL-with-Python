# Stock Data ETL with Python
Built a Python-based data pipeline to fetch SBI stock price data using yFinance, store it in Supabase PostgreSQL, and visualize trends using Matplotlib.
![im](https://github.com/user-attachments/assets/c85f8007-6eeb-46ff-998d-f84448d88e2f)

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
</head>
<body>
  <h1>sbin-stock-pipeline/</h1>
  <ul>
    <li>
      <strong>scripts/</strong> – Python scripts for ETL and visualization
      <ul>
        <li><code>load.py</code> – Fetches SBIN stock data and uploads to Supabase</li>
        <li><code>cleandata.py</code> – Reads from Supabase and plots the Close price</li>
      </ul>
    </li>
    <li>
      <strong>assets/</strong> – Images, plots, or diagrams used in README
      <ul>
        <li><code>pipeline_diagram.png</code> – The image you generated</li>
      </ul>
    </li>
    <li><code>README.md</code> – Project overview and instructions</li>
  </ul>
</body>
</html>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>SBIN Stock Data Pipeline</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 40px;
      background-color: #f8f9fa;
      color: #333;
    }
    h1 {
      color: #004080;
    }
    .container {
      max-width: 800px;
      margin: auto;
    }
    img {
      width: 100%;
      height: auto;
      border: 1px solid #ccc;
      border-radius: 8px;
      margin-top: 20px;
    }
    p {
      font-size: 16px;
      line-height: 1.6;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>SBIN Stock Price Data Pipeline</h1>
    <p>This image represents the end-to-end data pipeline where historical stock price data for <strong>SBIN</strong> is fetched using Python, stored in a Supabase PostgreSQL database, and visualized using Matplotlib.</p>

    <img src="https://github.com/user-attachments/assets/1e3214b0-378b-4357-a563-47052d1fbc92" alt="sbin pipeline diagram">

    <p>
      <strong>Tools Used:</strong> yFinance, SQLAlchemy, Supabase, PostgreSQL, Matplotlib, Python.
    </p>
  </div>
</body>
</html>

