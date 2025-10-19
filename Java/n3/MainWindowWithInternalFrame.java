import javax.swing.*;
import java.awt.*;

public class MainWindowWithInternalFrame {
    public static void main(String[] args) {
        // Create the main window (JFrame)
        JFrame mainFrame = new JFrame("Main Window");
        mainFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        mainFrame.setSize(800, 600);
        mainFrame.setLocationRelativeTo(null); // Center the window

        // Create a desktop pane to hold internal frames
        JDesktopPane desktopPane = new JDesktopPane();
        mainFrame.setContentPane(desktopPane);

        // Create an internal window
        JInternalFrame internalFrame = new JInternalFrame(
            "Internal Window",
            true,  // Resizable
            true,  // Closable
            true,  // Maximizable
            true   // Minimizable
        );
       
        // Set up the internal frame
        internalFrame.setSize(300, 200);
        internalFrame.setLocation(50, 50);
        internalFrame.setVisible(true);
       
        // Add components to the internal frame
        JLabel label = new JLabel("Hello from Internal Window!", SwingConstants.CENTER);
        internalFrame.add(label, BorderLayout.CENTER);
       
        // Add the internal frame to the desktop pane
        desktopPane.add(internalFrame);

        // Make the main window visible
        mainFrame.setVisible(true);
    }
}