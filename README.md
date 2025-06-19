# Stock Data ETL with Python
Built a Python-based data pipeline to fetch SBI stock price data using yFinance, store it in Supabase PostgreSQL, and visualize trends using Matplotlib.
![im](https://github.com/user-attachments/assets/c85f8007-6eeb-46ff-998d-f84448d88e2f)

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>SBIN Stock Pipeline Project Structure</title>
</head>
<body>
  <h1>sbin-stock-pipeline/</h1>
  <ul>
    <li>
      <strong>scripts/</strong> – Python scripts for ETL and visualization
      <ul>
        <li><code>load.py</code> – Fetches SBIN stock data and uploads to Supabase</li>
        <li><code>plotdata.py</code> – Reads from Supabase and plots the Close price</li>
      </ul>
    </li>
    <li>
      <strong>assets/</strong> – Images, plots, or diagrams used in README
      <ul>
        <li><code>pipeline_diagram.png</code> – The image you generated</li>
      </ul>
    </li>
    <li><code>README.md</code> – Project overview and instructions</li>
    <li><code>requirements.txt</code> – Python dependencies</li>
  </ul>
</body>
</html>
