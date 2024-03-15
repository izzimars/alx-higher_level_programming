if __name__ == "__main__":
    import hidden_4
    for name in sorted(dir(hidden_4)):
        if name[0] != '_' and name[1] != '_':
            print(name)
