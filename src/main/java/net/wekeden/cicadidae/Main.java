package net.wekeden.cicadidae;

import java.io.IOException;

/**
 * Hello world!
 *
 */
public class Main {
    public static void main(String[] args) throws IOException {
        Config config = new Config();
        config.setServer("irc.freenode.net");
        config.setPort(6667);
        config.setUsername("bestbotever");
        config.setNick("bestbotever");

        IrcConnection connection = new IrcConnection(config);
        connection.connect();
    }
}
