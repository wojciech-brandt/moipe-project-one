clc
clear

data = readmatrix("preliminary.csv");

figOpt = {'Position', [300, 300, 300, 500], 'DefaultAxesFontSize', 13};

f1 = figure(figOpt{:});
plot(data(1,:), data(2,:), 'r*')
grid;
xlabel("czas [s]");
ylabel("napięcie [V]");