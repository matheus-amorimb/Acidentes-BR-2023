import matplotlib.pyplot as plt

import numpy as np

colors_ref = ['#1d3557', '#457b9d', '#a8dadc', '#e63946', '#f1faee']
plt.style.use('fivethirtyeight')
plt.rc('figure', figsize=(15,8))
plt.rc('xtick', labelsize=14)
plt.rc('ytick', labelsize=14)

def plot_bar(x, height, titulo, subtitulo = "", colors = colors_ref[0], rotation = 0, legend = "", x_labels = "", titulo_x_pos = 0, titulo_y_pos = 0,
            display_data = ""):
    
    x_ = x
    height_ = height
    legend_ = legend
    colors_ = colors
    rotation_ = rotation
    titulo_ = titulo
    subtitulo_ = subtitulo
    titulo_x_pos_ = titulo_x_pos
    titulo_y_pos_ = titulo_y_pos
    display_data_ = display_data
    
    fig, ax = plt.subplots();
    
    ax.bar(x = x_, 
           height = height_, 
           label = legend_,
           color = colors_,
           edgecolor="black",
           linewidth=1.5,);
    
    if x_labels != "":
        x_labels_ = x_labels
    else:
        x_labels_ = ax.get_xticklabels()
    
    ax.set_xticklabels(labels = x_labels_, 
                       rotation = rotation_,
                       weight = 'bold');
    
    if titulo_x_pos != 0:
        titulo_x_pos_ = titulo_x_pos
    else:
        titulo_x_pos_ = -2
    
    if titulo_y_pos != 0:
        titulo_y_pos_ = titulo_y_pos
    else: 
        titulo_y_pos_ = max(ax.get_yticks())
    
    ax.text(x = titulo_x_pos_ , y = titulo_y_pos_ * 1.2, 
            s = titulo_, 
            fontsize = 26, 
            weight = 'bold', horizontalalignment = "left")
    
    ax.text(x = titulo_x_pos_ , y = titulo_y_pos_ * 1.12, 
            s = subtitulo_, 
            fontsize = 18,  
            alpha = .85)
    
    for value, bar in enumerate(ax.patches):
        x = bar.get_x() + bar.get_width()/2
        y = bar.get_height() * 1.04
        
        if display_data_ == "percentage":
            display = f'{height_[value]/sum(height_)*100:.1f}%'
        else:
            display = height_[value]
            
        ax.text(x, y, 
                s = display, 
                fontsize = 12,
                weight = 'bold',
                horizontalalignment='center')

    if legend != "":
        ax.legend(loc="right");
    
    ax.xaxis.grid(False);
    
    plt.tight_layout();
    plt.show();

def plot_hbar(y, width, titulo, subtitulo = "", colors = colors_ref[0], rotation = 0, legend = "", y_labels = "", titulo_x_pos = 0, titulo_y_pos = 0,
            display_data = "", height = 0.8, width_size = 15, fmt = "", total = ""):
    
    y_ = y
    width_ = width
    legend_ = legend
    colors_ = colors
    rotation_ = rotation
    titulo_ = titulo
    subtitulo_ = subtitulo
    titulo_x_pos_ = titulo_x_pos
    titulo_y_pos_ = titulo_y_pos
    display_data_ = display_data
    height_ = height
    width_size_ = width_size
    
    if width_size != 15:
        width_size_ = width_size
    
    fig, ax = plt.subplots(figsize=(width_size_,8));
    
    container = ax.barh(y = y_, 
                       width = width_, 
                       label = legend_,
                       color = colors_, 
                       height = height_,               
                       edgecolor="black",
                       linewidth=1.5,);
    
    
    if total == "":
        total_ = width
    else:
        total_ = total
    
    if fmt == "":
        fmt_ = '{:.0f}'
    else:
        fmt_ = lambda x: '{:.1f}%'.format((x*100)/sum(total_))

    ax.bar_label(container, 
                 padding = 8, 
                 weight = 'bold', 
                 fmt = fmt_)
    
    if y_labels != "":
        y_labels_ = y_labels
    else:
        y_labels_ = ax.get_yticklabels()
    
    ax.set_yticklabels(labels = y_labels_, 
                       rotation = rotation_,
                       fontsize = 12,
                       weight = 'bold');
    
    if titulo_x_pos != 0:
        titulo_x_pos_ = titulo_x_pos
    else:
        titulo_x_pos_ = -2
    
    if titulo_y_pos != 0:
        titulo_y_pos_ = titulo_y_pos
    else: 
        titulo_y_pos_ = max(ax.get_yticks())
    
    ax.text(x = titulo_x_pos_ , y = titulo_y_pos_ * 1.2, 
            s = titulo_, 
            fontsize = 26, 
            weight = 'bold')
    
    ax.text(x = titulo_x_pos_ , y = titulo_y_pos_ * 1.11, 
            s = subtitulo_, 
            fontsize = 18,  
            alpha = .85)

    if legend_ != "":
        ax.legend(loc="right");
    
    ax.yaxis.grid(False);
    
    ax.vlines(x=0, 
              ymin = (container[0].get_y() - height_/2), 
              ymax = (container[-1].get_y() + height_), 
              colors = "black")
    
    plt.tight_layout();
    plt.show();

def plot_stacked_bar(x, dict_heights, titulo, subtitulo = "", colors = colors_ref[0], rotation = 0, legend = "", x_labels = "", titulo_x_pos = 0, titulo_y_pos = 0,
            display_data = "", width = 0.8):
    
    x_ = x
    dict_heights_ = dict_heights
    legend_ = legend
    colors_ = colors
    rotation_ = rotation
    titulo_ = titulo
    subtitulo_ = subtitulo
    titulo_x_pos_ = titulo_x_pos
    titulo_y_pos_ = titulo_y_pos
    display_data_ = display_data
    width_ = width
    
    fig, ax = plt.subplots();
    
    base = np.zeros(len(x_))

    for i, (classificacao, dict_height) in enumerate(dict_heights_.items()):
        container = ax.bar(x = x_, 
                           height = dict_height, 
                           label = classificacao,
                           bottom = base,
                           color = colors_[i],
                           edgecolor="black",
                           linewidth=1.5,
                           width = width_);

        base += dict_height
        
    ax.bar_label(container, 
                 padding = 8)

    if x_labels != "":
        x_labels_ = x_labels
    else:
        x_labels_ = ax.get_xticklabels()
    
    ax.set_xticklabels(labels = x_labels_, 
                       rotation = rotation_,
                       weight = 'bold');
    
    if titulo_x_pos != 0:
        titulo_x_pos_ = titulo_x_pos
    else:
        titulo_x_pos_ = -2
    
    if titulo_y_pos != 0:
        titulo_y_pos_ = titulo_y_pos
    else: 
        titulo_y_pos_ = max(ax.get_yticks())
    
    ax.text(x = titulo_x_pos_ , y = titulo_y_pos_ * 1.2, 
            s = titulo_, 
            fontsize = 26, 
            weight = 'bold', horizontalalignment = "left")
    
    ax.text(x = titulo_x_pos_ , y = titulo_y_pos_ * 1.12, 
            s = subtitulo_, 
            fontsize = 18,  
            alpha = .85)
    
    if legend_ != "":
        ax.legend(labels=legend_)
    else:
        ax.legend()
        
    ax.xaxis.grid(False);
    
    plt.tight_layout();
    plt.show();

def plot_stacked_barh(y, dict_heights, titulo, subtitulo = "", colors = colors_ref[0], rotation = 0, legend = "", y_labels = "", titulo_x_pos = 0, titulo_y_pos = 0,
            display_data = "", height = 0.8):
    
    y_ = y
    dict_heights_ = dict_heights
    legend_ = legend
    colors_ = colors
    rotation_ = rotation
    titulo_ = titulo
    subtitulo_ = subtitulo
    titulo_x_pos_ = titulo_x_pos
    titulo_y_pos_ = titulo_y_pos
    display_data_ = display_data
    height_ = height
    
    fig, ax = plt.subplots();
    
    base = np.zeros(len(y_))

    for i, (classificacao, dict_height) in enumerate(dict_heights_.items()):
        container = ax.barh(y = y_, 
                           width = dict_height, 
                           label = classificacao,
                           left = base,
                           color = colors_[i],
                           edgecolor="black",
                           linewidth=1.5,
                           height = height_);

        base += dict_height
        
    ax.bar_label(container, 
                 padding = 8,                 
                 weight = 'bold', 
                 fmt = lambda x: '{:.1f}%'.format((x*100)/sum(base)))

    if y_labels != "":
        y_labels_ = y_labels
    else:
        y_labels_ = ax.get_yticklabels()
    
    ax.set_yticklabels(labels = y_labels_, 
                       rotation = rotation_,
                       weight = 'bold');
    
    if titulo_x_pos != 0:
        titulo_x_pos_ = titulo_x_pos
    else:
        titulo_x_pos_ = -2
    
    if titulo_y_pos != 0:
        titulo_y_pos_ = titulo_y_pos
    else: 
        titulo_y_pos_ = max(ax.get_yticks())
    
    ax.text(x = titulo_x_pos_ , y = titulo_y_pos_ * 1.2, 
            s = titulo_, 
            fontsize = 26, 
            weight = 'bold', horizontalalignment = "left")
    
    ax.text(x = titulo_x_pos_ , y = titulo_y_pos_ * 1.12, 
            s = subtitulo_, 
            fontsize = 18,  
            alpha = .85)
    
    if legend_ != "":
        ax.legend(labels=legend_, loc = "lower right")
    else:
        ax.legend()
        
    ax.yaxis.grid(False);
    
    ax.vlines(x=0, 
              ymin = (container[0].get_y() - height_/2), 
              ymax = (container[-1].get_y() + height_), 
              colors = "black")
    
    plt.tight_layout();
    plt.show();