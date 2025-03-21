import "./style.css";

import React from "react";
import { JoyLayout } from '../layouts/JoyLayout';
import { Header } from "../components/Header";
import { Box } from "@mui/joy";

export const LayoutDefault = ({ children }: { children: React.ReactNode }) => {
  return (
    <JoyLayout>
      <Box
        sx={{
          display: 'flex',
          flexDirection: 'column',
          minHeight: '100vh',
        }}
      >
        <Header />
        <Box
          sx={{
            display: 'flex',
            flexDirection: 'column',
            flexGrow: 1,
          }}
        >
          {children}
        </Box>
      </Box>
    </JoyLayout >
  );
}
