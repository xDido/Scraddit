"use client";

import { Button } from "@/components/ui/button";
import { Menu, MoveRight, X } from "lucide-react";
import { useState } from "react";
import Link from "next/link";
import { FaGithub } from "react-icons/fa6";

export const Header1 = () => {
const navigationItems = [
    {
    title: "Home",
    href: "/",
    description: "",
    },
    {
    title: "Product",
    description: "Managing a small business today is already tough.",
    items: [
        {
        title: "Reports",
        href: "/reports",
        },
        {
        title: "Statistics",
        href: "/statistics",
        },
        {
        title: "Dashboards",
        href: "/dashboards",
        },
        {
        title: "Recordings",
        href: "/recordings",
        },
    ],
    },
    {
    title: "Company",
    description: "Managing a small business today is already tough.",
    items: [
        {
        title: "About us",
        href: "/about",
        },
        {
        title: "Fundraising",
        href: "/fundraising",
        },
        {
        title: "Investors",
        href: "/investors",
        },
        {
        title: "Contact us",
        href: "/contact",
        },
    ],
    },
];

const [isOpen, setOpen] = useState(false);
return (
    <header className="w-full z-40 fixed top-0 left-0 bg-background">
    <div className="container relative mx-auto min-h-20 flex gap-4 flex-row lg:grid lg:grid-cols-3 items-center">
        <div className="justify-start items-center gap-4 lg:flex hidden flex-row">
      <Button variant="ghost" className="hidden md:inline">
            Home
        </Button>
        </div>
        <div className="flex lg:justify-center">
        <p className="font-semibold">Scraddit</p>
        </div>
        <div className="flex justify-end w-full gap-4">
        <div className="border-r hidden md:inline"></div>
        <Button variant="outline">FAQ</Button>
            <Button><FaGithub></FaGithub> </Button>
        </div>
        <div className="flex w-12 shrink lg:hidden items-end justify-end">
        <Button variant="ghost" onClick={() => setOpen(!isOpen)}>
            {isOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
        </Button>
        {isOpen && (
            <div className="absolute top-20 border-t flex flex-col w-full right-0 bg-background shadow-lg py-4 container gap-8">
            {navigationItems.map((item) => (
                <div key={item.title}>
                <div className="flex flex-col gap-2">
                    {item.href ? (
                    <Link
                        href={item.href}
                        className="flex justify-between items-center"
                    >
                        <span className="text-lg">{item.title}</span>
                        <MoveRight className="w-4 h-4 stroke-1 text-muted-foreground" />
                    </Link>
                    ) : (
                    <p className="text-lg">{item.title}</p>
                    )}
                    {item.items &&
                    item.items.map((subItem) => (
                        <Link
                        key={subItem.title}
                        href={subItem.href}
                        className="flex justify-between items-center"
                        >
                        <span className="text-muted-foreground">
                            {subItem.title}
                        </span>
                        <MoveRight className="w-4 h-4 stroke-1" />
                        </Link>
                    ))}
                </div>
                </div>
            ))}
            </div>
        )}
        </div>
    </div>
    </header>
);
};