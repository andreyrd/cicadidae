package net.wekeden.cicadidae;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.Queue;
import java.util.concurrent.ConcurrentLinkedQueue;

/**
 * Created by Andrey on 9/7/2014.
 */
public class IrcConnection extends Thread {
    private Queue<String> commands;

    private Config config;

    private Socket socket;
    private BufferedReader reader;
    private PrintWriter writer;

    private static final String END = "\r\n";

    public IrcConnection(Config config) {
        this.commands = new ConcurrentLinkedQueue<String>();
        this.config = config;
    }

    public void connect() throws IOException {
        socket = new Socket(config.getServer(), config.getPort());
        reader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        writer = new PrintWriter(socket.getOutputStream());

        start();
    }

    @Override
    public void run() {
        writer.print("USER " + config.getNick() + " 0 * :" + config.getUsername() + END);
        writer.print("NICK " + config.getNick() + END);
        writer.flush();

        while (socket.isConnected()) {
            try {
                System.out.println(reader.readLine());
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

        try {
            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
