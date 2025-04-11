from dataclasses import dataclass

@dataclass
class Project:
    title: str
    subtitle: str
    description: str
    link: str
    linkText: str
    buttonImgPath: str

    @staticmethod
    def from_dict(data: dict):
        return Project(
            title=data.get("title"),
            subtitle=data.get("subtitle"),
            description=data.get("description"),
            link=data.get("link"),
            linkText=data.get("linkText"),
            buttonImgPath=data.get("buttonImgPath")
        )
    
    def to_dict(self):
        return {
            "title": self.title,
            "subtitle": self.subtitle,
            "description": self.description,
            "link": self.link,
            "linkText": self.linkText,
            "buttonImgPath": self.buttonImgPath
        }

projects = [
    {
        "title": "SimpleMusic Transfer",
        "subtitle": "Swift/Web API Playlist Transfer App",
        "description": "SimpleMusic is an app that allows users to match and transfer playlists across platforms. Built using SwiftUI, SwiftData, MusicKit, and the Spotify Web API, SimpleMusic provides an easy-to-use interface that makes transferring playlists straightforward.",
        "link": "https://github.com/jharrisong830/SimpleMusic",
        "linkText": "View on GitHub",
        "buttonImgPath": "/link_icons/github-mark.svg"
    },
    {
        "title": "Groovy",
        "subtitle": "Spotify Battle Ranking React App",
        "description": "Users can select tracks from an artist (fetched from the Spotify Web API) and rank them through a series of head-to-head \"battles\". Technologies used include React, TypeScript, and Redis.",
        "link": "https://github.com/jharrisong830/cs554-team10",
        "linkText": "View on GitHub",
        "buttonImgPath": "/link_icons/github-mark.svg"
    },
    {
        "title": "SimpleHW",
        "subtitle": "Pure Swift/SwiftUI App",
        "description": "A simple app for keeping track of homework assignments. Add classes, assignments, due dates, and notifications. Separate from my coursework and self-taught with online resources and documentation from Apple.",
        "link": "https://github.com/jharrisong830/SimpleHW",
        "linkText": "View on GitHub",
        "buttonImgPath": "/link_icons/github-mark.svg"
    },
    {
        "title": "Tweeter",
        "subtitle": "Full-stack Web App for Sharing Music",
        "description": "Tweeter is a social media application where posts are centered around music. Each post has an attached song, album, or user playlist that other users can like and comment on. Music data is drawn using the Spotify Web API.",
        "link": "https://github.com/jharrisong830/cs546-group7",
        "linkText": "View on GitHub",
        "buttonImgPath": "/link_icons/github-mark.svg"
    },
    {
        "title": "jhg.app (this site!)",
        "subtitle": "Personal Website Written in React",
        "description": "My website has evolved over the past couple of years. It started as a static HTML site. I made it look nicer and a bit more dynamic using Bootstrap and server-side rendering with Flask. Now, I've re-written it with React (create-react-app).",
        "link": "https://github.com/jharrisong830/jhg-app",
        "linkText": "View on GitHub",
        "buttonImgPath": "/link_icons/github-mark.svg"
    },
    {
        "title": "dotfiles",
        "subtitle": "Terminal Config and Scripts",
        "description": "This repository holds all of my terminal configuration files, which I use across macOS and Windows (and Linux if I need to use it). It also contains setup scripts (shell script for macOS, batch script for Windows) to create symlinks for all necessary files, so that changes in the repository can easily be synced.",
        "link": "https://github.com/jharrisong830/dotfiles",
        "linkText": "View on GitHub",
        "buttonImgPath": "/link_icons/github-mark.svg"
    }
]