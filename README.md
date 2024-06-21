<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

</head>
<body>

  <h1>Steganography Detection Tool</h1>

  <p>This repository contains Python scripts to detect steganography in image (PNG) and audio (WAV/MP3) files using LSB (Least Significant Bit) analysis.</p>

  <h2>Features</h2>

  <ul>
    <li>Detect steganography in PNG images by analyzing LSB planes.</li>
    <li>Detect steganography in WAV and MP3 audio files by analyzing LSB of audio samples.</li>
  </ul>

  <h2>Installation</h2>

  <h3>Requirements</h3>

  <ul>
    <li>Python 3.6 or above</li>
  </ul>

  <h3>Dependencies</h3>

  <p>Install the required Python libraries using pip:</p>

  <pre><code>pip install numpy matplotlib pydub</code></pre>

  <h3>Setup</h3>



<p><strong>Clone the repository:</strong></p>
<pre><code>git clone https://github.com/your-username/steganography-detection.git</code></pre>

<p><strong>Navigate to the project directory:</strong></p>
<pre><code>cd steganography-detection</code></pre>

<p><strong>Optionally, create a virtual environment:</strong></p>
<pre><code>python -m venv venv</code></pre>
<pre><code>source venv/bin/activate   <!-- On Windows use `venv\Scripts\activate` --></code></pre>

<p><strong>Install dependencies:</strong></p>
<pre><code>pip install -r requirements.txt</code></pre>


  <h2>Usage</h2>

  <h3>Detecting Steganography in PNG Images</h3>

  <ol>
    <li>Run the image steganography detection script:</li>
    <pre><code>python image_steg_detection.py</code></pre>

    <li>Enter the path to the PNG image file when prompted.</li>
  </ol>

  <h3>Detecting Steganography in WAV/MP3 Audio Files</h3>

  <ol>
    <li>Run the audio steganography detection script:</li>
    <pre><code>python audio_steg_detection.py</code></pre>

    <li>Enter the path to the WAV or MP3 audio file when prompted.</li>
  </ol>

  <h2>Contributing</h2>

  <p>Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.</p>

</body>
</html>
