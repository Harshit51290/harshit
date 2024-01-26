import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class resumebulide extends JFrame {

    private JTextArea resumeTextArea;
 
    public resumebulide() {
        initializeUI();
    }

    private void initializeUI() {
        setTitle("Resume Builder");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel panel = new JPanel();
        panel.setLayout(new BoxLayout(panel, BoxLayout.Y_AXIS));

        JLabel nameLabel = new JLabel("Name:");
        JTextField nameField = new JTextField();
        JLabel experienceLabel = new JLabel("Experience:");
        JTextField experienceField = new JTextField();
        JLabel skillsLabel = new JLabel("Skills:");
        JTextField skillsField = new JTextField();

        JButton generateButton = new JButton("Generate Resume");

        resumeTextArea = new JTextArea();
        resumeTextArea.setEditable(false);

        generateButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String name = nameField.getText();
                String experience = experienceField.getText();
                String skills = skillsField.getText();

                String resume = generateResume(name, experience, skills);
                resumeTextArea.setText(resume);

                saveResumeToFile(resume);
            }
        });

        panel.add(nameLabel);
        panel.add(nameField);
        panel.add(experienceLabel);
        panel.add(experienceField);
        panel.add(skillsLabel);
        panel.add(skillsField);
        panel.add(generateButton);
        panel.add(new JScrollPane(resumeTextArea));

        add(panel);

        setVisible(true);
    }

    private String generateResume(String name, String experience, String skills) {
        StringBuilder resume = new StringBuilder();
        resume.append("Name: ").append(name).append("\n\n");
        resume.append("Experience: ").append(experience).append("\n\n");
        resume.append("Skills: ").append(skills);
        return resume.toString();
    }

    private void saveResumeToFile(String resume) {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter("resume.txt"))) {
            writer.write(resume);
            writer.flush();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new resumebulide());
    }
}
