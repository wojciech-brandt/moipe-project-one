clc
clear

data = readmatrix("main.csv");

figOpt = {'Position', [300, 300, 800, 500], 'DefaultAxesFontSize', 13};

f1 = figure(figOpt{:});
plot(data(1,:), data(2,:), 'r*')
grid;
xlabel("czas [dni]");
ylabel("temperatura [°C]");