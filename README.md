<details open>
  <summary><h2>🗺️ Repository Map</h2></summary>
  <pre>
Python-GUI-Projects/
├──  project1[paint_software].py       * Main Paint application script
├──  Project2[Notebook].py             * Text editor application script
├──  Project2[Notebook_demo_text].txt  * Sample data for the notebook
├──  Project3[Tic_Tac_Toe_game].py     * Tic-Tac-Toe game logic and GUI
├──  LICENSE                           * MIT License file
└──  README.md                         * Project documentation
  </pre>
</details>

<hr />

<h2> Detailed Project Breakdowns</h2>

<table width="100%">
  <tr>
    <td width="30%" align="center">
      <br><b>🎨 Paint Software</b><br>
      <code>Tkinter Canvas</code>
    </td>
    <td>
      <p>A canvas-based architecture that captures mouse coordinates to draw lines and shapes in real-time.</p>
      <ul>
        <li><b>Tech Stack:</b> Python, Tkinter (Canvas, Button, Scale)</li>
        <li><b>Key Logic:</b> Uses <code>event.x</code> and <code>event.y</code> to bind drawing functions to drag events.</li>
      </ul>
    </td>
  </tr>
  
  <tr>
    <td width="30%" align="center">
      <br><b>📝 Notebook Editor</b><br>
      <code>File I/O</code>
    </td>
    <td>
      <p>A GUI utility for handling <code>.txt</code> files, demonstrating file system integration with a UI.</p>
      <ul>
        <li><b>Tech Stack:</b> Python, Tkinter (Text, Menu, filedialog)</li>
        <li><b>Key Logic:</b> Implements <code>open</code> and <code>save</code> methods using Python’s built-in I/O operations.</li>
      </ul>
    </td>
  </tr>

  <tr>
    <td width="30%" align="center">
      <br><b>❌ Tic-Tac-Toe</b><br>
      <code>Game Logic</code>
    </td>
    <td>
      <p>A logic-heavy grid game featuring automated win detection and state management.</p>
      <ul>
        <li><b>Tech Stack:</b> Python, Tkinter (Button, messagebox)</li>
        <li><b>Key Logic:</b> 
          <i>Win Conditions:</i> Checks all 8 possible combinations (rows, cols, diagonals). <br>
          <i>Tie Handling:</i> Detects board saturation (9 moves) without a winner.
        </li>
      </ul>
    </td>
  </tr>
</table>