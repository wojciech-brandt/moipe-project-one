clc
clear

data = readmatrix("preliminary.csv");

figOpt = {'Position', [300, 300, 300, 500], 'DefaultAxesFontSize', 13};

f1 = figure(figOpt{:});
plot(data(1,:), data(2,:), 'r*')
grid;
xlabel("czas [dni]");
ylabel("temperatura [°C]");

figOpt = {'Position', [300, 300, 800, 500], 'DefaultAxesFontSize', 13};

f2 = figure(figOpt{:});
histfit(data(2,:));
xlabel("temperatura [°C]");
ylabel("liczebność");
grid;

